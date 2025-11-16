from fastapi import APIRouter, HTTPException
from .schemas import Workout, WorkoutCreate
from .services import add_workout, get_all_workouts, get_workout

router = APIRouter()

@router.get("/", response_model=list[Workout])
def list_workouts():
    return get_all_workouts()

@router.get("/{workout_id}", response_model=Workout)
def read_workout(workout_id: int):
    workout = get_workout(workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout

@router.post("/", response_model=Workout, status_code=201)
def create_workout(payload: WorkoutCreate):
    return add_workout(payload)
