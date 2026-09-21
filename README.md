# BAW Knowledge MCP — IBM BAW / CP4BA expertise for your AI agent

**Endpoint:** `https://bawmcp.dosvak.com/mcp` (Model Context Protocol, Streamable HTTP, no account, free)
**Status page:** https://bawmcp.dosvak.com

A public MCP server that gives IBM Bob, Claude Code, Cursor, VS Code and any other MCP-capable agent the working knowledge
behind the Dosvak IBM Business Automation Workflow projects:

- **authoring method** for process applications (generate-build-import-verify, OOB UI Toolkit, client-side human services, service
  flows, business objects, teams, BPDs) and the delivery checklist;
- **engine facts** verified on BPM 8.6.2, BAW 26 and CP4BA 25.0.1: task visibility and claiming, search index limits, timers and the
  event manager, snapshot / migration semantics, `/ops` operations, coach rendering quirks;
- **REST APIs**: the engine's own v1 catalogue (172 calls with parameters), the v2 / `/ops` / federated map, CP4BA prefixes and sign-on;
- **TWX package structure** for offline authoring and the import pitfalls on traditional and CP4BA targets;
- **coach / UI guidelines**, security (users, teams, LDAP / VMM, CSRF), operations and tuning, troubleshooting map;
- **designs** of the published utility apps (Operations, Process Tools REST, Failed Instance Triage, Instance Migration Console,
  Container Version Manager, Instance Purge, Task Lists, Test Data Generator, Headless Process Portal);
- **install runbooks**: BAW 26 traditional single node (Db2, WAS ND, IHS, Case), Workflow Server, OpenLDAP lab directory, ODM 9.6 on
  Liberty, FileNet CPE 5.7 on WAS 9;
- the **TWX Code Analyzer rule catalogue** (156 `TCA-*` rules with what they check and how to fix) so agents write code that passes review;
- **how-to recipes** (e-mail, REST with auth, UCA / timers, REST-driven processes, team filters, documents, ODM, migration, install, BPMConfig,
  tests, coach tables, EPV / env vars, errors, purge, import troubleshooting, custom views, SQL, building an app step by step, generated TWX,
  LDAP, CP4BA delivery, performance, export / artifact source, CI/CD + scenario tests) and **build + test guides per artifact type**;
- **product topics**: App Connect, FileNet + Navigator, ODM, Case, BAI / Kafka / PDW, PFS / Workplace / portals, the designers, OpenShift
  cluster setup and a CP4BA operator install guide (marked unvalidated until we run it);
- the **product database schema** (682 tables) and **reference tooling** (43 scripts) on request.

## Connect

IBM Bob — `~/.bob/settings/mcp.json` (every workspace) or `.bob/mcp.json` (one workspace):

```json
{ "mcpServers": { "baw-knowledge": { "url": "https://bawmcp.dosvak.com/mcp" } } }
```

Claude Code:

```bash
claude mcp add --transport http baw-knowledge https://bawmcp.dosvak.com/mcp
```

Cursor / VS Code / Windsurf / Continue / custom clients: the same URL as an HTTP (streamable-http) MCP server — see [clients/](clients/).

## What your agent gets

| Tool | Use |
|---|---|
| `ask(question, budget?, version?, category?)` | one call: the best passages for a question with topic ids to cite |
| `search_knowledge(query, category?, kinds?, version?, limit?)` | hybrid search (synonyms such as CSHS / UCA / EPV / PDW understood) over topics, analyzer rules, REST calls, database tables |
| `get_topic(id)`, `get_section(id, heading)`, `related(id)`, `list_categories()`, `list_topics(category?)` | read and browse: method, authoring, how-to, artifacts (build + test per artifact type), general, products, designs, cp4ba, ocp, install, headless, analyzer |
| `search_rules(query?, category?, severity?)`, `get_rule(id)` | code-quality rules (`TCA-APP-002`, `TCA-SVC-013`, ...) |
| `rest_endpoint(query, api?)` | REST calls of the classic v1 API, v2 and `/ops` with method, path and parameters |
| `db_schema(table or words, db?)` | product database tables and columns (BPMDB 8.6.2, basdb CP4BA 25.0.1) for reporting SQL |
| `authoring_checklist(target?)` | the delivery checklist for traditional, CP4BA or both |
| `list_tools(query?)`, `get_tool(name)` | reference tooling on request: Python harnesses (direct flow runs, Playwright coach sweeps, imports, design sweeps, CP4BA sign-on), generators, wsadmin / shell scripts, SQL, JS API code |
| `submit_feedback(...)`, `suggest_topic(title, why, outline?, relatedTo?)` | tell us what was missing or wrong; propose new topics — BAW / CP4BA-related subjects only |

Resources `baw://topic/{id}`, `baw://rules`, `baw://rest`, `baw://guide`; prompts `design-process-app` and `review-twx`.
Topics drafted but not yet validated are marked as such in every result; verified facts say "verified on <version>".

**Agent skill**: [skills/baw-knowledge/SKILL.md](skills/baw-knowledge/SKILL.md) tells IBM Bob / Claude Code when and how to use the server —
copy it into your skills folder (`~/.claude/skills/baw-knowledge/`, Bob's skills directory).

Try: *"With the baw-knowledge tools, design a console that purges finished instances on CP4BA, list the REST calls it needs and the
analyzer rules its service flows must respect, and cite the topics you used."*

## Feedback

Open an issue in this repository or call `submit_feedback` from your agent. Zero-result searches and feedback are reviewed to extend the
knowledge base.

## Terms

The service is provided as is and free of charge, rate limited, and may change without notice. Calls are logged (timestamp, tool, query
text, returned ids, client name / user agent, a hashed client address, feedback) to improve the knowledge base and for training; no
credentials or personal data are requested — do not send any in queries. Content © Dosvak LLC. IBM, Business Automation Workflow and
Cloud Pak are trademarks of IBM Corporation; this is an independent service, not affiliated with or endorsed by IBM.
Related open source: [twx-code-analyzer](https://github.com/dosvak/twx-code-analyzer), [generic-ui-toolkit](https://github.com/dosvak/generic-ui-toolkit),
[operations-cp4ba](https://github.com/dosvak/operations-cp4ba), [headless-process-portal](https://github.com/dosvak/headless-process-portal).
