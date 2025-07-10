from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_database_initialization():
    db = Database()

    assert len(db.buns) == 3
    assert isinstance(db.buns[0], Bun)

    assert len(db.ingredients) == 6
    assert isinstance(db.ingredients[0], Ingredient)

def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert isinstance(buns, list)
    assert all(isinstance(b, Bun) for b in buns)
    assert [bun.get_name() for bun in buns] == ["black bun", "white bun", "red bun"]

def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert isinstance(ingredients, list)
    assert all(isinstance(i, Ingredient) for i in ingredients)
    names = [i.get_name() for i in ingredients]
    assert names == [
        "hot sauce", "sour cream", "chili sauce",
        "cutlet", "dinosaur", "sausage"
    ]