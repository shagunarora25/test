import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def _load_mock_data(filename: str):
    with open(BASE_DIR / "mock_data" / filename, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_jira_status():
    """Returns mock JIRA release tracking data."""
    return _load_mock_data("deployments.json")
