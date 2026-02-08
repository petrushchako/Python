from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Define variables and their types
    api_key: str
    debug: bool
    port: int
    engine: str = "Docker"

    # Load .env file
    model_config = SettingsConfigDict(env_file=".env")


# Instantiate settings
settings = Settings()

print(f"{settings.api_key=}")
print(f"{settings.debug=}")
print(f"{settings.port=}")
print(f"{settings.engine=}")