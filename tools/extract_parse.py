"""
Tool: extract_parse
Launches a document extraction job (OCR).

Input schema:
{
  "document_base64": "<base64-encoded-pdf>",
  "doc_type": "invoice",
  "version": "18.0",
  "webhook_url": "https://your-callback.example.com"  # optional
}

Output schema:
{
  "document_token": "abc123",
  "status": "processing"
}

Sample input:
{
  "document_base64": "<base64-encoded-pdf>",
  "doc_type": "invoice",
  "version": "18.0"
}
"""

from controllers.extract_client import ExtractClient

def extract_parse(document_base64: str, doc_type: str, version: str, webhook_url: str = None):
    """
    Launches a document extraction job.
    """
    client = ExtractClient()
    return client.extract_parse(document_base64, doc_type, version, webhook_url)
