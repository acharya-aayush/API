from fastapi import APIRouter, HTTPException
from .schemas import Recipe, RecipeSearch
from .services import find_recipes, get_recipe

router = APIRouter()

@router.get("/", response_model=list[Recipe])
def search_recipes(ingredient: str | None = None, max_minutes: int | None = None):
    request = RecipeSearch(ingredient=ingredient, max_minutes=max_minutes)
    return find_recipes(request)

@router.get("/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int):
    recipe = get_recipe(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
