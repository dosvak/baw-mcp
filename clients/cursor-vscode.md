# Cursor, VS Code (Copilot agent mode), Windsurf, Continue

Cursor `~/.cursor/mcp.json` or `.cursor/mcp.json`:
```json
{ "mcpServers": { "baw-knowledge": { "url": "https://bawmcp.dosvak.com/mcp" } } }
```
VS Code `.vscode/mcp.json`:
```json
{ "servers": { "baw-knowledge": { "type": "http", "url": "https://bawmcp.dosvak.com/mcp" } } }
```
Any client built on the MCP SDKs: `StreamableHTTPClientTransport(new URL("https://bawmcp.dosvak.com/mcp"))`.
