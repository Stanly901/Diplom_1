import pytest
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "Ketchup", 0.4),
    ("FILLING", "Bacon", 1.5),
    ("FILLING", "Cheese", 1.2),
])
def test_ingredient_attributes(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price