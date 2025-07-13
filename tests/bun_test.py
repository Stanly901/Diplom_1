import pytest
from praktikum.bun import Bun
from data.test_data import BUNS

class TestBun:

    @pytest.mark.parametrize("name, price", BUNS)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUNS)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price