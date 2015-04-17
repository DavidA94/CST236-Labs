from behave import *
from source.Cities import Cities
from source.City import City


@given("1 - 10 cities")
def impl_step(context):
    context.cities = Cities()
    context.city1 = City("ABC", (10, 10), 56)

@then("Get more accurate picture")
def impl_step(context):
    result1 = context.cities.calc_route(context.city1)
    result2 = context.cities.calc_route(context.city1, context.city1,
                                        context.city1, context.city1,
                                        context.city1, context.city1,
                                        context.city1, context.city1,
                                        context.city1, context.city1)

    assert result1 == result2 == "More accurate picture"


@given("0 or 11+ cities")
def impl_step(context):
    context.cities = Cities()
    context.city1 = "CityName"


@then("Get error")
def impl_step(context):
    result1 = context.cities.calc_route(context.city1, context.city1,
                                        context.city1, context.city1,
                                        context.city1, context.city1,
                                        context.city1, context.city1,
                                        context.city1, context.city1,
                                        context.city1)

    result2 = context.cities.calc_route()

    assert result1 == "Error: Too many cities"
    assert result2 == "Please pass cities"