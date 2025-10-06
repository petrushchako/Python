import os
import requests
import sys
import time
import argparse

"""
Enable secret scanning (and optionally push protection) across all repos in an org.

Usage:
  export GITHUB_TOKEN="ghp_..."      # PAT or app token with proper scopes
  python3 enable_secret_scanning.py my-org --push-protection --skip-archived

Notes:
  - Token needs 'repo' or 'security_events' (private repos) or 'public_repo' (public-only).
"""

API = "https://api.github.com"
TOKEN = None

HEADERS = {
    "Accept": "application/vnd.github+json",
}

# Basic retry helper
def do_request(method, url, **kwargs):
    headers = kwargs.pop("headers", {})
    headers.update(HEADERS)
    headers["Authorization"] = f"Bearer {TOKEN}"
    for attempt in range(1, 5):
        resp = requests.request(method, url, headers=headers, timeout=30, **kwargs)
        if resp.status_code in (200, 201, 204):
            return resp
        if resp.status_code in (429, 502, 503, 504):
            backoff = 2 ** attempt
            print(f"Transient error {resp.status_code}, retrying in {backoff}s...", file=sys.stderr)
            time.sleep(backoff)
            continue
        # non-retryable
        return resp
    return resp

def list_org_repos(org, per_page=100):
    url = f"{API}/orgs/{org}/repos"
    params = {"per_page": per_page, "page": 1, "type":"all"}
    while True:
        resp = do_request("GET", url, params=params)
        if resp.status_code != 200:
            raise SystemExit(f"Failed to list repos: {resp.status_code} {resp.text}")
        data = resp.json()
        if not data:
            break
        for r in data:
            yield r
        # pagination via Link headers
        link = resp.headers.get("Link", "")
        if 'rel="next"' not in link:
            break
        # increment page (simple)
        params["page"] += 1

def enable_secret_scanning(owner, repo, enable_push_protection=False):
    url = f"{API}/repos/{owner}/{repo}"
    payload = {
        "security_and_analysis": {
            "secret_scanning": {"status": "enabled"},
        }
    }
    if enable_push_protection:
        payload["security_and_analysis"]["secret_scanning_push_protection"] = {"status": "enabled"}

    resp = do_request("PATCH", url, json=payload)
    return resp

def main():
    p = argparse.ArgumentParser()
    p.add_argument("org", help="GitHub organization")
    p.add_argument("--token-env", default="GITHUB_TOKEN", help="Env var name for token")
    p.add_argument("--push-protection", action="store_true", help="Also enable push protection")
    p.add_argument("--skip-archived", action="store_true", help="Skip archived repos")
    p.add_argument("--skip-forks", action="store_true", help="Skip forks")
    args = p.parse_args()

    global TOKEN
    TOKEN = os.getenv(args.token_env)
    if not TOKEN:
        raise SystemExit(f"Set ${args.token_env} with a token that has 'repo' or 'security_events' scope")

    org = args.org
    success = []
    failed = []

    for r in list_org_repos(org):
        name = r["name"]
        owner = r["owner"]["login"]
        if args.skip_archived and r.get("archived"):
            print(f"Skipping archived: {owner}/{name}")
            continue
        if args.skip_forks and r.get("fork"):
            print(f"Skipping fork: {owner}/{name}")
            continue

        print(f"Enabling secret scanning for {owner}/{name} ...", end=" ")
        resp = enable_secret_scanning(owner, name, enable_push_protection=args.push_protection)
        if resp.status_code in (200, 201, 204):
            print("OK")
            success.append(f"{owner}/{name}")
        else:
            print(f"FAIL {resp.status_code}: {resp.text}")
            failed.append((f"{owner}/{name}", resp.status_code, resp.text))

    print("\nSummary:")
    print(f"  Success: {len(success)}")
    print(f"  Failed: {len(failed)}")
    if failed:
        for f in failed:
            print("  -", f)

if __name__ == "__main__":
    main()
