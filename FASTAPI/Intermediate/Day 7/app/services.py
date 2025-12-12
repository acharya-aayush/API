from typing import Optional, List
from .schemas import RequestCreate, RequestPatch, ServiceRequest, RequestStatus

requests: List[ServiceRequest] = [
    ServiceRequest(id=1, title="Server setup", description="Provision the new staging environment.", status=RequestStatus.open, note=None)
]

_next_id = 2


def get_all_requests() -> List[ServiceRequest]:
    return requests


def get_request(request_id: int) -> Optional[ServiceRequest]:
    return next((item for item in requests if item.id == request_id), None)


def create_request(payload: RequestCreate) -> ServiceRequest:
    global _next_id
    request = ServiceRequest(id=_next_id, status=RequestStatus.open, note=None, **payload.model_dump())
    requests.append(request)
    _next_id += 1
    return request


def patch_request(request_id: int, payload: RequestPatch) -> Optional[ServiceRequest]:
    request = get_request(request_id)
    if request is None:
        return None
    if payload.status is not None:
        request.status = payload.status
    if payload.note is not None:
        request.note = payload.note
    return request
