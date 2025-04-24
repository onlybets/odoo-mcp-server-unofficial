"""
Tool: list_models
Returns models visible to the current user (delegates to ir.model).

Input schema: none
Output schema:
[
  {
    "model": "res.partner",
    "name": "Contact"
  },
  ...
]

Sample output:
[
  {"model": "res.partner", "name": "Contact"},
  {"model": "crm.lead", "name": "Lead"}
]
"""

from controllers.odoo_client import OdooClient

def list_models():
    """
    Returns a list of models visible to the current user.
    """
    client = OdooClient()
    return client.list_models()
