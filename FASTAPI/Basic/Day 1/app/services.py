from typing import Optional
from .schemas import Workout, WorkoutCreate

workouts: list[Workout] = [
    Workout(id=1, title="Morning run", duration_minutes=30, notes="Easy pace")
]

_next_id = 2


def get_all_workouts() -> list[Workout]:
    return workouts


def get_workout(workout_id: int) -> Optional[Workout]:
    return next((item for item in workouts if item.id == workout_id), None)


def add_workout(payload: WorkoutCreate) -> Workout:
    global _next_id
    workout = Workout(id=_next_id, **payload.model_dump())
    workouts.append(workout)
    _next_id += 1
    return workout
