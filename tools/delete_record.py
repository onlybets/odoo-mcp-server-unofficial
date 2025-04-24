"""
Tool: delete_record
Deletes one or more records in a model.

Input schema:
{
  "model": "res.partner",
  "ids": [42, 43]
}

Output schema:
{
  "success": true
}

Sample input:
{
  "model": "res.partner",
  "ids": [42]
}
"""

from controllers.odoo_client import OdooClient

def delete_record(model: str, ids: list):
    """
    Deletes one or more records in a model.
    """
    client = OdooClient()
    result = client.delete_record(model, ids)
    return {"success": bool(result)}
