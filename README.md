# Odoo MCP Server

[![MCP](https://img.shields.io/badge/MCP-Server-blue)](https://modelcontextprotocol.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**High-level, secure access to Odoo 18.0 (JSON-RPC) and Odoo Extract API for OCR document parsing.**

---

## 🚀 Quick Start with Cline

1. **Clone the repo:**
   ```bash
   git clone https://github.com/onlybets/odoo-mcp-server-unofficial.git
   cd odoo-mcp-server-unofficial
   ```

2. **Configure credentials:**
   ```bash
   cp .env.example .env
   # Edit .env and fill in your Odoo/Extract credentials
   ```

3. **Run with Cline (no self-hosting needed):**
   - Cline auto-runs the server locally for you.
   - Just open the repo in Cline and start using the tools!

---

## 🛠️ Tools & JSON Schemas

### 1. `list_models`
Returns models visible to the current user.

**Input:** none  
**Output:**  
```json
[
  {"model": "res.partner", "name": "Contact"},
  {"model": "crm.lead", "name": "Lead"}
]
```

---

### 2. `get_fields`
Returns fields & metadata for a model.

**Input:**  
```json
{ "model": "res.partner" }
```
**Output:**  
```json
{
  "id": {"string": "ID", "type": "integer", "required": true, "readonly": true},
  "name": {"string": "Name", "type": "char", "required": true, "readonly": false}
}
```

---

### 3. `search_read`
Searches and reads records from a model.

**Input:**  
```json
{
  "model": "res.partner",
  "domain": [["is_company", "=", true]],
  "fields": ["id", "name", "email"],
  "limit": 10
}
```
**Output:**  
```json
[
  {"id": 7, "name": "Acme Corp", "email": "info@acme.com"}
]
```

---

### 4. `create_record`
Creates a new record in a model.

**Input:**  
```json
{
  "model": "res.partner",
  "values": {"name": "New Partner", "email": "new@partner.com"}
}
```
**Output:**  
```json
{ "id": 42 }
```

---

### 5. `update_record`
Updates one or more records in a model.

**Input:**  
```json
{
  "model": "res.partner",
  "ids": [42],
  "values": {"email": "updated@partner.com"}
}
```
**Output:**  
```json
{ "success": true }
```

---

### 6. `delete_record`
Deletes one or more records in a model.

**Input:**  
```json
{
  "model": "res.partner",
  "ids": [42]
}
```
**Output:**  
```json
{ "success": true }
```

---

### 7. `extract_parse`
Launches a document extraction job.

**Input:**  
```json
{
  "document_base64": "<base64-encoded-pdf>",
  "doc_type": "invoice",
  "version": "18.0"
}
```
**Output:**  
```json
{ "document_token": "abc123", "status": "processing" }
```

---

### 8. `extract_get_result`
Fetches the result of a document extraction job.

**Input:**  
```json
{
  "doc_type": "invoice",
  "version": "18.0",
  "document_token": "abc123"
}
```
**Output:**  
```json
{
  "status": "done",
  "data": { "invoice_number": "INV-001", "total": 123.45 }
}
```

---

## 🐳 Docker Compose

- Run all services with:
  ```bash
  docker-compose up --build
  ```
- Works out-of-the-box for local dev and testing.

---

## 🧪 CI/CD

- GitHub Actions workflow (`.github/workflows/ci.yml`) runs:
  - `pylint` (with odoo plugin if available)
  - `pytest` (runs smoke tests)
- Matrix for Python 3.11+.

---

## 📄 License

MIT License. See [LICENSE](LICENSE).

---

> **MCP Server** — Model Context Protocol  
> [https://modelcontextprotocol.org/](https://modelcontextprotocol.org/)
