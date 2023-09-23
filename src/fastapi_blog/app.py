from fastapi import FastAPI

from fastapi_blog.config import Config


def app_factory():
    config = Config()
    app = FastAPI(title=config.blog_name, description=config.blog_description)


    @app.get("")
    def home():
        return "<insert frontend code here>"

    @app.get("/posts/{post_id}")
    def get_markdown(post_id: str):
        return config.markdown_posts_folder / f"{post_id}.md"
