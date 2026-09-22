---
name: baw-knowledge
description: Use the baw-knowledge MCP server for any IBM BAW / BPM / CP4BA question - designing, building, testing, deploying, operating or troubleshooting process applications, coaches, service flows, REST APIs (v1, v2, /ops, federated), TWX packages, snapshots, Case, ODM, FileNet, App Connect, LDAP, install, OpenShift for CP4BA, performance and code quality. Trigger on words like BAW, BPM, CP4BA, Cloud Pak, Workflow Center, Process Center, BPD, coach, human service, service flow, TWX, toolkit, snapshot, UCA, EPV, FileNet, ODM, Case Builder, Workplace.
---

# baw-knowledge

The `baw-knowledge` MCP server (public endpoint `https://bawmcp.dosvak.com/mcp`) holds verified engine and REST facts, authoring
method, how-to recipes, artifact build / test guides, product topics, install runbooks, the analyzer rule catalogue, the REST
catalogues (v1 / v2 / ops), the product database schema and reference tooling.

## Method

1. Start with `ask(question)` - it returns the best passages with topic ids. Read the ids you rely on with `get_topic` when you need the
   full text; `get_section(id, heading)` for large topics; `related(id)` to widen.
2. For an API call use `rest_endpoint(query, api?)`; for a database table `db_schema(table)`; for a code-quality question
   `search_rules(query, category?, severity?)`.
3. Before delivering an app, run `authoring_checklist(target)` and walk it; for a test plan read `artifact-test-strategy-overview` and the
   `artifact-*` topics of the artifact types involved.
4. To build or generate a process app / TWX, call `build_kit()` first and follow its order of work: `get_package(words)` (a tested package may
   already exist), then `get_tool('twxkit.py')` + `get_tool('twxkit_sample.py')` and the reference topic `howto-build-a-twx-from-scratch`.
   Never hand-write TWX object XML, a manifest or product uuids from memory - such packages do not import. Tools flagged
   `[needs unserved: ...]` by `list_tools` are design references only, not something to re-implement.
5. When tooling is needed (running flows over REST, Playwright coach sweeps, imports, sign-on, generators), call `list_tools(query)` and
   `get_tool(name)` and adapt the settings (hosts, users are placeholders).
6. Cite topic ids in your answer. Prefer facts tagged with the user's platform version (`version` filter: 8.6.2, 24, 26, cp4ba25, saas).
7. If the answer is weak or missing, tell the user and call `submit_feedback`; propose genuinely missing BAW / CP4BA subjects with
   `suggest_topic` (related topics only).
