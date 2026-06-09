import json
from pathlib import Path

import requests


BASE_DIR = Path(__file__).resolve().parent.parent


def _load_mock_data(filename: str):
    with open(BASE_DIR / "mock_data" / filename, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_pipelines():
    """Returns mock pipeline data for the UI."""
    return _load_mock_data("pipelines.json")


def trigger_pipeline(branch: str = "main"):
    """Placeholder method for future GitLab API integration."""
    return {
        "status": "queued",
        "message": f"Mock pipeline triggered for branch {branch}.",
        "branch": branch,
    }


def retry_pipeline(pipeline_id: int):
    """Placeholder method for a retry action."""
    return {
        "status": "restarted",
        "message": f"Mock retry requested for pipeline {pipeline_id}.",
        "pipeline_id": pipeline_id,
    }


def get_pipeline_logs():
    """Placeholder for log retrieval from GitLab."""
    return _load_mock_data("logs.json")


def get_gitlab_health():
    """Placeholder for a health check request."""
    try:
        requests.get("https://gitlab.example.test/health", timeout=2)
        return "healthy"
    except requests.RequestException:
        return "mock"
