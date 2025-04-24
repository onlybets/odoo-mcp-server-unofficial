import logging
import requests
import time
from typing import Any, Dict, Optional

from src.config import Config

logger = logging.getLogger("odoo-mcp-server.extract_client")

class ExtractClient:
    def __init__(self):
        self.url = Config.ODOO_URL.rstrip("/") + "/extract/document"
        self.account_token = Config.EXTRACT_ACCOUNT_TOKEN
        self.session = requests.Session()

    def extract_parse(self, document_base64: str, doc_type: str, version: str, webhook_url: Optional[str] = None):
        params = {
            "account_token": self.account_token,
            "document_base64": document_base64,
            "doc_type": doc_type,
            "version": version
        }
        if webhook_url:
            params["webhook_url"] = webhook_url
        return self._json_rpc("parse", params)

    def extract_get_result(self, doc_type: str, version: str, document_token: str):
        params = {
            "account_token": self.account_token,
            "doc_type": doc_type,
            "version": version,
            "document_token": document_token
        }
        return self._json_rpc("get_result", params)

    def _json_rpc(self, method: str, params: dict):
        url = self.url
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": int(time.time() * 1000)
        }
        start = time.time()
        try:
            logger.info("[API] Extract request: %s", str(payload)[:256])
            resp = self.session.post(url, json=payload)
            resp.raise_for_status()
            result = resp.json()
            if "error" in result:
                logger.error("[API] Extract error: %s", result["error"])
                raise Exception(result["error"])
            return result.get("result")
        except Exception as e:
            logger.error("[Error] Failed with: %s", str(e))
            raise
        finally:
            elapsed = time.time() - start
            logger.info("[API] Extract %s completed in %.2fs", method, elapsed)
