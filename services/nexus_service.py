import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def _load_mock_data(filename: str):
    with open(BASE_DIR / "mock_data" / filename, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_artifacts():
    """Returns mock Nexus artifact metadata."""
    return _load_mock_data("artifacts.json")


def create_artifact(name: str, version: str):
    """Placeholder method for future artifact creation."""
    return {"status": "created", "name": name, "version": version}


def promote_artifact(name: str, target: str):
    """Placeholder method for artifact promotion."""
    return {"status": "promoted", "name": name, "target": target}
