from behave import *
from source.Cities import Cities
from source.City import City


@given("A new Cities object with a starting city")
def impl_step(context):
    context.cities = Cities(start_city=City("Wilsonville", (10, 40), 56))


@then("set the starting city")
def impl_step(context):
    assert context.cities.start_point == City("Wilsonville", (10, 40), 56)