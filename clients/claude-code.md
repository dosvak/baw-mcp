# Claude Code

```bash
claude mcp add --transport http baw-knowledge https://bawmcp.dosvak.com/mcp        # user scope
claude mcp add --transport http --scope project baw-knowledge https://bawmcp.dosvak.com/mcp   # writes .mcp.json in the repo
```
or in `.mcp.json`: `{ "mcpServers": { "baw-knowledge": { "type": "http", "url": "https://bawmcp.dosvak.com/mcp" } } }`
