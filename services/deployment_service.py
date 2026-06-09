import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def _load_mock_data(filename: str):
    with open(BASE_DIR / "mock_data" / filename, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_deployments():
    """Returns mock deployment history."""
    return _load_mock_data("deployments.json")


def get_approvals():
    """Returns mock release approvals."""
    return _load_mock_data("approvals.json")


def deploy_release(environment: str, release_name: str):
    """Placeholder method for deployment orchestration."""
    return {"status": "queued", "environment": environment, "release_name": release_name}


def approve_release(release_name: str):
    """Placeholder approval action."""
    return {"status": "approved", "release_name": release_name}


def reject_release(release_name: str):
    """Placeholder rejection action."""
    return {"status": "rejected", "release_name": release_name}
