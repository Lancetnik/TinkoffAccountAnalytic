from pathlib import Path

from pydantic import BaseSettings


__all__ = ("settings",)


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"


class Settings(BaseSettings):
    base_dir: Path = BASE_DIR
    debug: bool = True

    class Config:
        frozen = True
        use_enum_values = True
        env_prefix = 'tin_app_'
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
        secrets_dir = CONFIG_DIR / "secrets"
        env_file = CONFIG_DIR / ".env.development"


settings = Settings()
