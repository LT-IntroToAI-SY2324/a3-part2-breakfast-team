from foodAndIngredients import foods_db
from match import match
from typing import List, Tuple, Callable, Any

def get_dish(foodAndIngredients: Tuple[str, List[str]]) -> str:
    return foodAndIngredients[0]

def get_ingredients(foodAndIngredients: Tuple[str, List[str]]) -> List[str]:
    return foodAndIngredients[1]

def dish_by_ingredients
# def title_by_actor(matches: List[str]) -> List[str]:
#     """Finds titles of all movies that the given actor was in

#     Args:
#         matches - a list of 1 string, just the actor

#     Returns:
#         a list of movie titles that the actor acted in
#     """
#     results = []
#     for movie in movie_db:
#         if matches[0] in get_actors(movie):
#             results.append(get_title(movie))
#     # print(results)
#     return results