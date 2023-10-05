from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest  # noqa: F401
from src.models.ingredient import Ingredient, Restriction  # noqa: F401


def test_dish():
    assert Dish('Espaguete', 1.99).name == 'Espaguete'

    assert hash(Dish('Espaguete', 1.99)) == hash(Dish('Espaguete', 1.99))
    assert hash(Dish('Espaguete', 1.99)) != hash(Dish('Strogonoff', 2.98))

    assert Dish('Espaguete', 1.99) == Dish('Espaguete', 1.99)
    assert Dish('Espaguete', 1.99) != Dish('Strogonoff', 2.98)

    assert repr(Dish('Espaguete', 1.99)) == "Dish('Espaguete', R$1.99)"

    with pytest.raises(TypeError):
        Dish('Espaguete', '1.99')
    with pytest.raises(ValueError):
        Dish('Espaguete', 0)

    new_dish = Dish('Espaguete', 1.99)
    new_ingredient = Ingredient('manteiga')
    new_dish.add_ingredient_dependency(new_ingredient, 1)

    assert new_dish.recipe.get(new_ingredient) == 1
    assert new_dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert new_dish.get_ingredients() == {new_ingredient}
