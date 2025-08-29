import re
from collections import Counter

log_file_path = "access.log"

# Regular expression
# \d+  - one or more digits (0–9)
# \.   - a literal dot (.) The backslash is needed because . by itself means "any character" in regex
# Example match: 192.168.0.1
ip_pattern = r"\d+\.\d+\.\d+\.\d+"


def analyze_log(log_file_path):
    with open(log_file_path) as file:
        log_lines = file.readlines()

    ip_addresses = re.findall(ip_pattern, "".join(log_lines))
    unique_ips = set(ip_addresses)
    num_requests = len(log_lines)

    url_counter = Counter()
    for line in log_lines:
        match = re.search(r'"GET (.*?) HTTP', line)
        if match:
            url = match.group(1)
            url_counter[url] += 1

    return num_requests, unique_ips, url_counter.most_common(3)


if __name__ == "__main__":
    num_requests, unique_ips, popular_urls = analyze_log(log_file_path)

    print("Log Analysis Results:")
    print(f"Number of Requests: \t\t{num_requests}")
    print(f"Number of Unique IP Addresses: \t{len(unique_ips)}")

    print("Popular URLs:")
    for url, count in popular_urls:
        print(f"{url}: {count} requests")
