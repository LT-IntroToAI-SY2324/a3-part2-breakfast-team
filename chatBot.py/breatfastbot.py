from foodAndIngredients import foods_db
from match import match
from typing import List, Tuple, Callable, Any

def get_dish(foodAndIngredients: Tuple[str, List[str]]) -> str:
    return foodAndIngredients[0]

def get_ingredients(foodAndIngredients: Tuple[str, List[str]]) -> List[str]:
    return foodAndIngredients[1]
