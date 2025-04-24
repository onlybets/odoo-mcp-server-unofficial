"""
Tool: create_record
Creates a new record in a model.

Input schema:
{
  "model": "res.partner",
  "values": {
    "name": "New Partner",
    "email": "new@partner.com"
  },
  "context": {"lang": "en_US"}
}

Output schema:
{
  "id": 42
}

Sample input:
{
  "model": "res.partner",
  "values": {
    "name": "New Partner",
    "email": "new@partner.com"
  }
}
"""

from controllers.odoo_client import OdooClient

def create_record(model: str, values: dict, context: dict = None):
    """
    Creates a new record in a model.
    """
    client = OdooClient()
    return {"id": client.create_record(model, values, context)}
