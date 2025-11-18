from typing import Optional
from .schemas import Recipe, RecipeSearch

recipes: list[Recipe] = [
    Recipe(id=1, title="Tomato Basil Pasta", ingredients=["tomato", "basil", "garlic"], cook_time_minutes=25, description="A quick weeknight pasta dish."),
    Recipe(id=2, title="Quick Chickpea Curry", ingredients=["chickpeas", "coconut milk", "curry powder"], cook_time_minutes=30),
]


def get_recipe(recipe_id: int) -> Optional[Recipe]:
    return next((item for item in recipes if item.id == recipe_id), None)


def find_recipes(search: RecipeSearch) -> list[Recipe]:
    results = recipes
    if search.ingredient:
        results = [item for item in results if search.ingredient.lower() in (ingredient.lower() for ingredient in item.ingredients)]
    if search.max_minutes is not None:
        results = [item for item in results if item.cook_time_minutes <= search.max_minutes]
    return results
