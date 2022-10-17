from pathlib import Path

from pydantic import BaseSettings


__all__ = ("settings",)


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    base_dir: Path = BASE_DIR
    debug: bool = False

    class Config:
        env_file = BASE_DIR / ".env.development"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
        secrets_dir = BASE_DIR / "config" / "secrets"
        frozen = True
        use_enum_values = True


settings = Settings()
