# Python Application to Read Vault Secrets (Local Execution)

This application reads secrets from a Vault instance running in a Docker container using the `hvac` Python library. The Python application itself will run locally on your machine.

## Prerequisites

- Docker installed on your system.
- Python 3.6 or higher.
- pip (Python package installer).

## Setup

1.  **Clone this repository (or create the `vault.py`, `requirements.txt`, and `setup.sh` files manually).**

2.  **Run the setup script:**
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```
    This script will:
    - Check if a local Vault Docker container named `local-vault` is running.
    - If not, it will start a development Vault instance on `http://localhost:8200`.
    - It will also remind you how to install Python dependencies and set environment variables.

3.  **Install Python Dependencies:**
    Navigate to the directory containing the files and run:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Environment Variables:**
    Before running the Python application, you need to set the following environment variables in your local environment:
    - `VAULT_ADDR`: The address of your Vault container (defaults to `http://localhost:8200`).
    - `VAULT_TOKEN`: A valid Vault token with read access to the desired secrets.
    - `VAULT_SECRET_PATH`: The path to the secret in Vault you want to read (defaults to `secret/data/my-app`).

    You can set these in your terminal before running the Python script, or you can use a `.env` file with the `python-dotenv` library (already installed via `requirements.txt`). If you choose to use a `.env` file, create a file named `.env` in the same directory as `vault.py` with the following format:

    ```
    VAULT_ADDR=http://localhost:8200
    VAULT_TOKEN=your_vault_token
    VAULT_SECRET_PATH=secret/data/my-app
    ```

    **Important:** For production environments, avoid hardcoding tokens or storing them in `.env` files. Use more secure methods for token management.

## Running the Application

1.  **Ensure the Vault container is running (if you didn't just run `setup.sh`):**
    ```bash
    docker start local-vault
    ```

2.  **Run the Python application:**
    ```bash
    python vault.py
    ```

    If you are using a `.env` file, the `load_dotenv()` function in `vault.py` will automatically load the environment variables before the script runs.

## Interacting with the Local Vault (Development Instance)

-   **Vault UI:** Access the Vault UI at `http://localhost:8200`. Use the root token `myroot` to log in.
-   **Vault CLI (inside the container):**
    ```bash
    docker exec -it local-vault sh
    vault status
    vault login myroot
    # Now you can perform Vault operations
    ```

## Example Usage

1.  Start the Vault container using `./setup.sh`.
2.  Log in to the Vault UI or CLI using the root token.
3.  Enable the Key/Value secrets engine (if not already enabled):
    ```bash
    docker exec -it local-vault sh
    vault secrets enable -path=secret kv-v2
    exit
    ```
4.  Write some secrets to the default path `secret/data/my-app`:
    ```bash
    vault kv put -address=http://localhost:8200 secret/data/my-app username="myuser" password="mypassword"
    ```
    (Note the explicit `-address` flag here since you're running this locally).
5.  Set the `VAULT_TOKEN` environment variable in your local terminal (e.g., `export VAULT_TOKEN="myroot"`) or in your `.env` file.
6.  Run the Python application: `python vault.py`.

You should see the `username` and `password` printed in your console.

## Cleaning Up

To stop and remove the local Vault container:

```bash
docker stop local-vault
docker rm local-vault