"""
Tool: extract_get_result
Fetches the result of a document extraction job.

Input schema:
{
  "doc_type": "invoice",
  "version": "18.0",
  "document_token": "abc123"
}

Output schema:
{
  "status": "done",
  "data": {
    "invoice_number": "INV-001",
    "total": 123.45,
    ...
  }
}

Sample input:
{
  "doc_type": "invoice",
  "version": "18.0",
  "document_token": "abc123"
}
"""

from controllers.extract_client import ExtractClient

def extract_get_result(doc_type: str, version: str, document_token: str):
    """
    Fetches the result of a document extraction job.
    """
    client = ExtractClient()
    return client.extract_get_result(doc_type, version, document_token)
