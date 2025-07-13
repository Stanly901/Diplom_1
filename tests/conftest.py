import pytest
from unittest.mock import Mock

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