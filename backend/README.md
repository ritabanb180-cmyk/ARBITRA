# ARBITRA backend

FastAPI + LangChain + LangGraph skeleton. Agents use an offline fake model, so no API keys are needed.

## Setup

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

On macOS/Linux, activate with `source .venv/bin/activate` and copy with `cp .env.example .env`.

## Run

```powershell
uvicorn app.main:app --reload
```

- Health: http://localhost:8000/api/v1/health
- Docs: http://localhost:8000/docs

## Test

```powershell
pytest
```

## Configuration

| Variable | Default | Values |
| --- | --- | --- |
| `ARBITRATION_STRATEGY` | `rule_based` | `rule_based`, `trust_weighting`, `calibration`, `meta_agent` |

Only `rule_based` is implemented; the others raise `NotImplementedError` until their TODOs are done.
