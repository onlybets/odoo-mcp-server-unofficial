# Odoo MCP Server Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install python-dotenv requests

# Optionally install MCP SDK if available
# RUN pip install mcp

ENV PYTHONUNBUFFERED=1

CMD ["python", "server.py"]
