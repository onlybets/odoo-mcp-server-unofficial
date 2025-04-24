"""
Tool: update_record
Updates one or more records in a model.

Input schema:
{
  "model": "res.partner",
  "ids": [42, 43],
  "values": {
    "email": "updated@partner.com"
  },
  "context": {"lang": "en_US"}
}

Output schema:
{
  "success": true
}

Sample input:
{
  "model": "res.partner",
  "ids": [42],
  "values": {
    "email": "updated@partner.com"
  }
}
"""

from controllers.odoo_client import OdooClient

def update_record(model: str, ids: list, values: dict, context: dict = None):
    """
    Updates one or more records in a model.
    """
    client = OdooClient()
    result = client.update_record(model, ids, values, context)
    return {"success": bool(result)}
