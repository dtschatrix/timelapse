from pydantic import BaseSettings
import os
class Settings(BaseSettings):
    server_host: str = "0.0.0.0"
    server_port: int = 1337
    
    POSTGRES_USER = "POSTGRES_USER"
    POSTGRES_PASSWORD = "POSTGRES_PASSWORD"
    POSTGRES_SERVER = "db"
    POSTGRES_PORT = "5432"
    POSTGRES_DB = "POSTGRES_DB"


settings = Settings(
    _env_file=".env",
    _env_file_encoding= "utf-8"
)