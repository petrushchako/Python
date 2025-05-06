import hvac
import os
from dotenv import load_dotenv

load_dotenv()

def read_vault_secrets():
    """Reads secrets from a Vault instance."""
    vault_addr = os.environ.get('VAULT_ADDR', 'http://localhost:8200')
    vault_token = os.environ.get('VAULT_TOKEN')
    secret_path = os.environ.get('VAULT_SECRET_PATH', 'secret/data/my-app')

    if not vault_token:
        print("Error: VAULT_TOKEN environment variable not set.")
        return

    try:
        client = hvac.Client(url=vault_addr, token=vault_token)
        read_response = client.secrets.kv.v2.read_secret(path=secret_path)
        if read_response and 'data' in read_response and 'data' in read_response['data']:
            secrets = read_response['data']['data']
            print("Secrets found in Vault:")
            for key, value in secrets.items():
                print(f"{key}: {value}")
        else:
            print(f"No secrets found at path: {secret_path}")
    except hvac.exceptions.VaultError as e:
        print(f"Error accessing Vault: {e}")

if __name__ == "__main__":
    read_vault_secrets()