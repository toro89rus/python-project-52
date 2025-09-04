import os

import dj_database_url
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.db_url = os.getenv("DATABASE_URL")
        self.secret_key = os.getenv("SECRET_KEY")
        self.rollbar_token = os.getenv("ROLLBAR_TOKEN")
        self.is_production = os.getenv("IS_PRODUCTION", "true") == "true"

    def setup_database(self, base_dir):
        if self.is_production:
            return dj_database_url.config(
                default=self.db_url,
                conn_max_age=600,
            )
        return {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": base_dir / "db.sqlite3",
        }

    @property
    def allowed_hosts(self):
        if self.is_production:
            return ["webserver", "task-manager-2c0i.onrender.com"]
        return ["localhost", "127.0.0.1"]
