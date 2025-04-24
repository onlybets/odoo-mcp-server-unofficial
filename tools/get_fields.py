"""
Tool: get_fields
Returns fields & metadata for a model (fields_get).

Input schema:
{
  "model": "res.partner"
}

Output schema:
{
  "id": {
    "string": "ID",
    "type": "integer",
    "required": true,
    "readonly": true
  },
  "name": {
    "string": "Name",
    "type": "char",
    "required": true,
    "readonly": false
  },
  ...
}

Sample input:
{
  "model": "res.partner"
}
"""

from controllers.odoo_client import OdooClient

def get_fields(model: str):
    """
    Returns fields and metadata for the given model.
    """
    client = OdooClient()
    return client.get_fields(model)
