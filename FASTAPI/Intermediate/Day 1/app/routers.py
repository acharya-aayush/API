from fastapi import APIRouter, HTTPException
from .schemas import Project, ProjectCreate
from .services import get_all_projects, get_project, create_project

router = APIRouter()

@router.get("/", response_model=list[Project])
def list_projects():
    return get_all_projects()

@router.get("/{project_id}", response_model=Project)
def read_project(project_id: int):
    project = get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/", response_model=Project, status_code=201)
def create_project_endpoint(payload: ProjectCreate):
    return create_project(payload)
