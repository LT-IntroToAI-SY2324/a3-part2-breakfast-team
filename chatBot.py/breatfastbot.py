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

def dishes_by_ingredient(matches: str) -> List[str]: 
    results = []
    for dish in foods_db:
        dishIngr = dish[1]
        if matches in dishIngr:
            results.append(dish[0])
    return results

def dish_by_ingredients(matches: List[str]) -> List[str]:
    results = []
    for dish in foods_db:
        dishIngr = dish[1]
        if dish in dishIngr:
            results.append(dish)
    return(results)

def what_to_make(matches: List[str]) -> List[str]: 
    results = []
    for dish in foods_db:
        dishIngr = dish[1]
        canMake = 0 
        for i in matches:
            if i in dishIngr:
                canMake += 1
            if canMake >= len(dishIngr):
                results.append(dish[0])
    return results




if __name__ == "__main__":
    assert isinstance(ingredients_by_dish(["Pancakes"]), list), "ingredients_by_dish not returning a list"
    assert isinstance(dishes_by_ingredient("Milk"), list), "ingredients_by_dish not returning a list"
    assert isinstance(what_to_make(["Potatoes", "Flour", "Salt", "Sugar", "Milk", "Butter", "Eggs"]), list), "ingredients_by_dish not returning a list"

    assert sorted(ingredients_by_dish(["Pancakes"])) == sorted(
        [
            "Flour", "Baking Powder", "Sugar", "Salt", "Milk", "Butter", "Eggs"
        ]
    )
    assert sorted(dishes_by_ingredient("Milk")) == sorted(
        [
            "Pancakes", "Ice Cream", "Cereal"
        ]
    )
    assert sorted(what_to_make(["Potatoes", "Flour", "Salt", "Sugar", "Milk", "Butter", "Eggs"])) == sorted(
        [
            "Pancakes", "Hash Browns"
        ]
    )