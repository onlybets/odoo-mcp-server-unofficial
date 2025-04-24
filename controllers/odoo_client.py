import logging
import requests
import time
from typing import Any, Dict, List, Optional

from src.config import Config

logger = logging.getLogger("odoo-mcp-server.odoo_client")

class OdooClient:
    def __init__(self):
        self.url = Config.ODOO_URL.rstrip("/")
        self.db = Config.ODOO_DB
        self.api_key = Config.ODOO_API_KEY
        self.login = Config.ODOO_LOGIN
        self.password = Config.ODOO_PASSWORD
        self.session = requests.Session()
        self.session_id = None

    def _headers(self):
        if self.api_key:
            return {"Authorization": f"Bearer {self.api_key}"}
        return {}

    def _json_rpc(self, method: str, params: dict, endpoint: str = "/jsonrpc"):
        url = f"{self.url}{endpoint}"
        headers = self._headers()
        payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": params,
            "id": int(time.time() * 1000)
        }
        start = time.time()
        try:
            logger.info("[API] Request to %s: %s", endpoint, str(payload)[:256])
            resp = self.session.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            result = resp.json()
            if "error" in result:
                logger.error("[API] Odoo error: %s", result["error"])
                raise Exception(result["error"])
            return result.get("result")
        except Exception as e:
            logger.error("[Error] Failed with: %s", str(e))
            raise
        finally:
            elapsed = time.time() - start
            logger.info("[API] %s completed in %.2fs", endpoint, elapsed)

    def authenticate(self):
        if self.api_key:
            return True
        params = {
            "db": self.db,
            "login": self.login,
            "password": self.password
        }
        result = self._json_rpc("call", params, endpoint="/web/session/authenticate")
        self.session_id = result.get("session_id")
        return self.session_id is not None

    def list_models(self) -> List[Dict[str, Any]]:
        # Delegates to ir.model
        params = {
            "service": "object",
            "method": "execute_kw",
            "args": [self.db, self._get_uid(), self._get_password(), "ir.model", "search_read", [[], ["model", "name"]]],
            "kwargs": {"context": self._get_context()}
        }
        return self._json_rpc("call", params)

    def get_fields(self, model: str) -> Dict[str, Any]:
        params = {
            "service": "object",
            "method": "execute_kw",
            "args": [self.db, self._get_uid(), self._get_password(), model, "fields_get", [], {"attributes": ["string", "type", "required", "readonly"]}],
            "kwargs": {"context": self._get_context()}
        }
        return self._json_rpc("call", params)

    def search_read(self, model: str, domain: list, fields: list, limit: int = 80, offset: int = 0, context: Optional[dict] = None):
        params = {
            "service": "object",
            "method": "execute_kw",
            "args": [self.db, self._get_uid(), self._get_password(), model, "search_read", [domain], {"fields": fields, "limit": limit, "offset": offset}],
            "kwargs": {"context": context or self._get_context()}
        }
        return self._json_rpc("call", params)

    def create_record(self, model: str, values: dict, context: Optional[dict] = None):
        params = {
            "service": "object",
            "method": "execute_kw",
            "args": [self.db, self._get_uid(), self._get_password(), model, "create", [values]],
            "kwargs": {"context": context or self._get_context()}
        }
        return self._json_rpc("call", params)

    def update_record(self, model: str, ids: list, values: dict, context: Optional[dict] = None):
        params = {
            "service": "object",
            "method": "execute_kw",
            "args": [self.db, self._get_uid(), self._get_password(), model, "write", [ids, values]],
            "kwargs": {"context": context or self._get_context()}
        }
        return self._json_rpc("call", params)

    def delete_record(self, model: str, ids: list):
        params = {
            "service": "object",
            "method": "execute_kw",
            "args": [self.db, self._get_uid(), self._get_password(), model, "unlink", [ids]],
            "kwargs": {"context": self._get_context()}
        }
        return self._json_rpc("call", params)

    def _get_uid(self):
        # TODO: Implement UID retrieval (cache after login)
        return 2  # Placeholder

    def _get_password(self):
        return self.api_key or self.password

    def _get_context(self):
        # TODO: Load context from config or session
        return {"lang": "en_US", "tz": "UTC"}
