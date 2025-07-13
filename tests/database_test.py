from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:

    def test_database_initialization(self):
        db = Database()
        assert len(db.buns) == 3
        assert isinstance(db.buns[0], Bun)
        assert len(db.ingredients) == 6
        assert isinstance(db.ingredients[0], Ingredient)

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(b, Bun) for b in buns)
        assert [bun.get_name() for bun in buns] == ["black bun", "white bun", "red bun"]

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(i, Ingredient) for i in ingredients)
        names = [i.get_name() for i in ingredients]
        assert names == [
            "hot sauce", "sour cream", "chili sauce",
            "cutlet", "dinosaur", "sausage"
        ]