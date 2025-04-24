import os
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

def get_env(key: str, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value

class Config:
    ODOO_URL = get_env("ODOO_URL", required=True)
    ODOO_DB = get_env("ODOO_DB", required=True)
    ODOO_API_KEY = get_env("ODOO_API_KEY")
    ODOO_LOGIN = get_env("ODOO_LOGIN")
    ODOO_PASSWORD = get_env("ODOO_PASSWORD")
    EXTRACT_ACCOUNT_TOKEN = get_env("EXTRACT_ACCOUNT_TOKEN")
    LOG_LEVEL = get_env("LOG_LEVEL", "INFO")
    WEBHOOK_URL = get_env("WEBHOOK_URL")

    @classmethod
    def as_dict(cls):
        return {
            "ODOO_URL": cls.ODOO_URL,
            "ODOO_DB": cls.ODOO_DB,
            "ODOO_API_KEY": bool(cls.ODOO_API_KEY),
            "ODOO_LOGIN": bool(cls.ODOO_LOGIN),
            "ODOO_PASSWORD": bool(cls.ODOO_PASSWORD),
            "EXTRACT_ACCOUNT_TOKEN": bool(cls.EXTRACT_ACCOUNT_TOKEN),
            "LOG_LEVEL": cls.LOG_LEVEL,
            "WEBHOOK_URL": bool(cls.WEBHOOK_URL),
        }
