from pathlib import Path

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    blog_name: str = "FastAPI Blog"
    blog_description: str = "A simple blog built with FastAPI"

    markdown_posts_folder: Path = Path("./posts")

