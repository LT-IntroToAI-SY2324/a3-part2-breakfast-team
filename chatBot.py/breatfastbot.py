from dish import foods_db
from match import match
from typing import List, Tuple, Callable, Any


def get_dish(dish: Tuple[str, List[str]]) -> str:
    return dish[0]

def get_ingredients(dish: Tuple[str, List[str]]) -> List[str]:
    return dish[1]



def ingredients_by_dish(matches: List[str]) -> List[str]: 
    results = []
    for dish in foods_db: 
        if get_dish(dish) == matches[0]:
            results = get_ingredients(dish)
    return results

def dishes_by_ingredient(matches: List[str]) -> List[str]: 
    results = []
    for dish in foods_db:
        dishIngr = dish[1]
        if dish in dishIngr:
            results.append(dish)
    return results

def dish_by_ingredients():

def what_to_make(): 





if __name__ == "__main__":
    assert isinstance(ingredients_by_dish(["Pancakes"]), list), "ingredients_by_dish not returning a list"

    assert sorted(ingredients_by_dish(["Pancakes"])) == sorted(
        [
            "Flour", "Baking Powder", "Sugar", "Salt", "Milk", "Butter", "Eggs"
        ]

    assert isinstance(), list), "ingredients_by_dish not returning a list"

    assert sorted() == sorted(
        [
            "Flour", "Baking Powder", "Sugar", "Salt", "Milk", "Butter", "Eggs"
        ]
    )