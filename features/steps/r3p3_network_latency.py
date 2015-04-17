from behave import *
from source.Cities import Cities
from source.City import City

@given("Two cities")
def impl_step(context):
    context.cities = Cities()
    context.cities.add_city(City("Wilsonville", (10, 50), 56))
    context.cities.add_city(City("Portland", (30, 45), 100))


@when("There is a network latency")
def impl_step(context):
    context.result = context.cities.latency_calc("Wilsonville", "Portland")


@then("Account for network latency")
def impl_step(context):
    assert context.result == "Network latency accounted for"