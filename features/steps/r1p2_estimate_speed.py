from behave import *
from source.Cities import Cities
from source.City import City

@given("I'm researching estimated speeds")
def step_impl(context):
    context.cities = Cities()
    context.cities.add_city(City("Wilsonville", (10, 50), 56))
    context.cities.add_city(City("Portland", (30, 45), 100))
    context.cities.add_city(City("Lake Oswego", (20, 60), 65))
    context.cities.add_city(City("Woodburn", (-10, 40), 65))

@when("given an estimated speed")
def step_impl(context):
    context.resultNetwork = context.cities.estimate_speed("Wilsonville", "Portland", 55)
    context.resultDriving = context.cities.estimate_speed("Wilsonville", "Lake Oswego", 250)

@then("determine if network or driving is faster")
def step_impl(context):
    assert context.resultDriving == "Driving is faster"
    assert context.resultNetwork == "Network is faster"
