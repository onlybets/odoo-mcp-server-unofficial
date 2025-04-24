import logging
import sys

from src.config import Config

# Setup logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("odoo-mcp-server")
logger.info("[Setup] Initializing Odoo MCP server...")

# Log config (no secrets)
logger.info("[Config] Loaded: %s", Config.as_dict())

# TODO: Import and initialize MCP SDK server
# from mcp.server import MCPServer

def main():
    # TODO: Register tool modules here
    logger.info("[Setup] MCP server would start here (MCP SDK not installed).")
    # Example:
    # server = MCPServer()
    # server.register_tool(...)
    # server.run()

if __name__ == "__main__":
    main()
