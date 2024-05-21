from pydantic_settings import BaseSettings, SettingsConfigDict

class BackendBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    POSTGRES_DB: str = model_config.get("POSTGRES_DB")
    POSTGRES_PASSWORD: str = model_config.get("POSTGRES_PASSWORD")
    POSTGRES_PORT: int = model_config.get("POSTGRES_PORT")
    POSTGRES_SCHEMA: str = model_config.get("POSTGRES_SCHEMA")
    POSTGRES_USERNAME: str = model_config.get("POSTGRES_USERNAME")
    POSTGRES_HOST: str = model_config.get("POSTGRES_HOST")
    POSTGRES_URL: str = model_config.get("POSTGRES_URL")
    
    
    JWT_SECRET_KEY: str = model_config.get("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = model_config.get("JWT_ALGORITHM")

    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]

    
    #SPECIFY PATH TO ENV AND DELETE ALL CONFIG.GET