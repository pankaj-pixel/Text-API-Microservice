from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    app_auth_token: str

    class Config:
        env_file = ".env"

# Instantiate the Settings
settings = Settings()

# Debugging: Print the loaded settings
print(f"Loaded auth token from Settings: {settings.app_auth_token}")
