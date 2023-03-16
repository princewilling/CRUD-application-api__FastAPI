from pydantic import BaseSettings, Field

class Settings(BaseSettings):

    database_name:str = Field(..., env='DATABASE_NAME')
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
