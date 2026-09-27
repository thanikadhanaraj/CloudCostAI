# CloudCost AI

CloudCost AI is a backend-first cloud cost optimization platform. Its planned MVP will ingest cloud billing and usage data, analyze costs, identify potential waste, and estimate savings.

## Current stage

This project is currently in the foundation stage. It contains a minimal FastAPI application and health endpoint; product features and data storage have not been added yet.

## Development setup

From the project root, create and activate a virtual environment, then install the project and development dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the test suite

```powershell
pytest
```

## Start the API

```powershell
uvicorn cloudcost_ai.main:app --reload
```

The health endpoint is available at `http://127.0.0.1:8000/health`.
