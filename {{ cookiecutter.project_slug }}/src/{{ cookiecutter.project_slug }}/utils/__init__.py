from pathlib import Path


def get_project_root() -> Path:
    project_root = Path(__file__).parent.parent.parent.parent

    return project_root
