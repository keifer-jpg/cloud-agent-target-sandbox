# cloud-agent-target-sandbox

Throwaway target repo for the Cloud Agent Orchestrator. The orchestrator clones this, branches,
runs SETUP_CMD + TEST_CMD in an isolated unprivileged user, and uses the result as the base-green
preflight. Keep `main` green.

- setup: `python -m venv .venv && .venv/bin/pip install -q -r requirements.txt`
- test:  `.venv/bin/pytest -q`
