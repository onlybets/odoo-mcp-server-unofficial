"""
Tool: search_read
Searches and reads records from a model.

Input schema:
{
  "model": "res.partner",
  "domain": [["is_company", "=", true]],
  "fields": ["id", "name", "email"],
  "limit": 10,
  "offset": 0,
  "context": {"lang": "en_US"}
}

Output schema:
[
  {
    "id": 7,
    "name": "Acme Corp",
    "email": "info@acme.com"
  },
  ...
]

Sample input:
{
  "model": "res.partner",
  "domain": [["is_company", "=", true]],
  "fields": ["id", "name", "email"],
  "limit": 10
}
"""

from controllers.odoo_client import OdooClient

def search_read(model: str, domain: list, fields: list, limit: int = 80, offset: int = 0, context: dict = None):
    """
    Searches and reads records from a model.
    """
    client = OdooClient()
    return client.search_read(model, domain, fields, limit, offset, context)
