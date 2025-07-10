import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("Sesame", 2.5),
    ("Brioche", 3.0),
    ("Potato", 1.99),
])
def test_bun_attributes(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price