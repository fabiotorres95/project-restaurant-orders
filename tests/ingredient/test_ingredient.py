from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    assert hash(Ingredient("queijo mussarela")) == hash(
        Ingredient("queijo mussarela")
    )

    assert hash(Ingredient("queijo mussarela")) != hash(Ingredient("tomate"))

    assert Ingredient("queijo mussarela") == Ingredient("queijo mussarela")
    assert Ingredient("queijo mussarela") != Ingredient("tomate")

    assert repr(
        Ingredient("queijo mussarela")
    ) == "Ingredient('queijo mussarela')"

    assert Ingredient("queijo mussarela").name == "queijo mussarela"
    assert Ingredient("queijo mussarela").restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }
