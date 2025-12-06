from typing import Optional
from .schemas import Project, ProjectCreate

projects: list[Project] = [
    Project(id=1, name="Website refresh", owner="emily", description="Update landing page and blog content.", tags=["web", "design"])
]

_next_id = 2


def get_all_projects() -> list[Project]:
    return projects


def get_project(project_id: int) -> Optional[Project]:
    return next((item for item in projects if item.id == project_id), None)


def create_project(payload: ProjectCreate) -> Project:
    global _next_id
    project = Project(id=_next_id, **payload.model_dump())
    projects.append(project)
    _next_id += 1
    return project
