import pytest
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient_1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_1

    @pytest.mark.parametrize("index, new_index", [
        (0, 1),
        (1, 0),
    ])
    def test_move_ingredient(self, index, new_index, mock_ingredient_1, mock_ingredient_2):
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
    def test_remove_ingredient(self, remove_index, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(remove_index)
        remaining = [mock_ingredient_2] if remove_index == 0 else [mock_ingredient_1]
        assert burger.ingredients == remaining

    def test_get_price(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        expected_price = 2.0 * 2 + 0.5 + 1.0
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        expected_price = mock_bun.get_price() * 2 + mock_ingredient_1.get_price() + mock_ingredient_2.get_price()
        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= filling {mock_ingredient_1.get_name()} =\n"
            f"= sauce {mock_ingredient_2.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {expected_price}"
        )

        actual_receipt = burger.get_receipt()
        assert actual_receipt == expected_receipt