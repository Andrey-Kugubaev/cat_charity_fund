from typing import Optional
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Donation service'
    description: str = 'Donation service for cats'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'UgFdnvDcSD',
    first_superuser_email: Optional[EmailStr] = 'andrey@ya.ru'
    first_superuser_password: Optional[str] = 'parolkarol'

    class Config:
        env_file = '.env'


settings = Settings()
