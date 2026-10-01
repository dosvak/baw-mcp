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
   A business process with user tasks (approval flow, lanes per team, gateways, loops) is built with `App.bpd()` and task coaches from
   `cshs(inputs=, outputs=, exits=)`: read `howto-build-a-process-with-user-tasks` and copy `get_tool('build_expkit.py')` (the verified
   Expense Approval Kit). Diagram rules that decide whether the result is usable in the designer: BPD node y is relative to its lane,
   buttons complete a task through coach exits, coach / service flow nodes need the designer's positive coordinates.
   Target: `build_kit(target)` with the user's platform; for CP4BA 24-26 build with twxkit `target='cp4ba'` (System Data
   8.6.0.0_TC, loopback `https://localhost:9443/bas` on the Studio, `/baw-<instance>` on a Process Server, LDAP team members). Deploy
   a snapshot created on the Center / Studio after the import (`get_tool('designer_snapshot.py')`), never the imported one - it has no
   compiled theme and renders unstyled on a server. On CP4BA, import without a browser with `get_tool('studio_import.py')`
   (REST import + validation + deployable snapshot). Coach event expressions have no `tw` object: pass inputs with
   `${Svc}.execute({...})`, never `tw.local.x = ...` (twxkit refuses it).
   Never hand-write TWX object XML, a manifest or product uuids from memory - such packages do not import. Tools flagged
   `[needs unserved: ...]` by `list_tools` are design references only, not something to re-implement.
5. When tooling is needed (running flows over REST, Playwright coach sweeps, imports, sign-on, generators), call `list_tools(query)` and
   `get_tool(name)` and adapt the settings (hosts, users are placeholders).
6. Cite topic ids in your answer. Prefer facts tagged with the user's platform version (`version` filter: 8.6.2, 24, 26, cp4ba24, cp4ba25, cp4ba26, saas).
7. If the answer is weak or missing, tell the user and call `submit_feedback`; propose genuinely missing BAW / CP4BA subjects with
   `suggest_topic` (related topics only).
