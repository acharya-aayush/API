from fastapi import APIRouter, HTTPException
from .schemas import RequestCreate, RequestPatch, ServiceRequest
from .services import get_all_requests, get_request, create_request, patch_request

router = APIRouter()

@router.get("/", response_model=list[ServiceRequest])
def list_requests():
    return get_all_requests()

@router.get("/{request_id}", response_model=ServiceRequest)
def read_request(request_id: int):
    request = get_request(request_id)
    if request is None:
        raise HTTPException(status_code=404, detail="Request not found")
    return request

@router.post("/", response_model=ServiceRequest, status_code=201)
def create_request_endpoint(payload: RequestCreate):
    return create_request(payload)

@router.patch("/{request_id}", response_model=ServiceRequest)
def patch_request_endpoint(request_id: int, payload: RequestPatch):
    request = patch_request(request_id, payload)
    if request is None:
        raise HTTPException(status_code=404, detail="Request not found")
    return request
