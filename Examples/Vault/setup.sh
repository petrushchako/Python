#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker is not installed. Please install it before running this script."
    exit 1
fi

# Check if Vault container is already running
VAULT_CONTAINER_NAME="local-vault"
if docker ps --filter name="$VAULT_CONTAINER_NAME" | grep -q "$VAULT_CONTAINER_NAME"; then
    echo "Vault container '$VAULT_CONTAINER_NAME' is already running."
else
    echo "Starting a local Vault container..."
    docker run -d --name "$VAULT_CONTAINER_NAME" --cap-add=IPC_LOCK -p 8200:8200 -p 8201:8201 vault:1.15.4 server -dev -dev-root-token-id="myroot"
    echo "Vault container started. Vault UI available at http://localhost:8200"
    echo "Development root token: myroot (for initial setup)"
    echo "Please initialize and unseal Vault if you haven't already."
    echo "For example, you can access the CLI inside the container:"
    echo "docker exec -it $VAULT_CONTAINER_NAME sh"
fi

echo "Python dependencies can be installed using: pip install -r requirements.txt"
echo "Remember to set the VAULT_ADDR and VAULT_TOKEN environment variables."
echo "You can also create a .env file with these variables."