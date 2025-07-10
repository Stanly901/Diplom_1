import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 2.0
    bun.get_name.return_value = "Test Bun"
    return bun

@pytest.fixture
def mock_ingredient_1():
    ing = Mock()
    ing.get_price.return_value = 0.5
    ing.get_name.return_value = "Lettuce"
    ing.get_type.return_value = "FILLING"
    return ing

@pytest.fixture
def mock_ingredient_2():
    ing = Mock()
    ing.get_price.return_value = 1.0
    ing.get_name.return_value = "Mayo"
    ing.get_type.return_value = "SAUCE"
    return ing


def test_set_buns(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient(mock_ingredient_1):
    burger = Burger()
    burger.add_ingredient(mock_ingredient_1)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient_1


@pytest.mark.parametrize("index, new_index", [
    (0, 1),
    (1, 0),
])
def test_move_ingredient(index, new_index, mock_ingredient_1, mock_ingredient_2):
    burger = Burger()
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)

    burger.move_ingredient(index, new_index)

    ingredients = [mock_ingredient_1, mock_ingredient_2]
    moved = ingredients.pop(index)
    ingredients.insert(new_index, moved)
    expected = ingredients

    assert burger.ingredients == expected


@pytest.mark.parametrize("remove_index", [0, 1])
def test_remove_ingredient(remove_index, mock_ingredient_1, mock_ingredient_2):
    burger = Burger()
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)
    burger.remove_ingredient(remove_index)
    remaining = [mock_ingredient_2] if remove_index == 0 else [mock_ingredient_1]
    assert burger.ingredients == remaining


def test_get_price(mock_bun, mock_ingredient_1, mock_ingredient_2):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)
    expected_price = 2.0 * 2 + 0.5 + 1.0
    assert burger.get_price() == expected_price


def test_get_receipt(mock_bun, mock_ingredient_1, mock_ingredient_2):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)

    receipt = burger.get_receipt().lower()
    assert "(==== test bun ====)" in receipt
    assert "= filling lettuce =" in receipt
    assert "= sauce mayo =" in receipt
    assert "price:" in receipt