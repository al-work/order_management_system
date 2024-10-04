import os


class Settings:
    DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/orders_db")
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")


settings = Settings()
