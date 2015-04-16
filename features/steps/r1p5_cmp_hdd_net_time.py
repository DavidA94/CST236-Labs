from behave import *
from source.City import City

@given("a speed and hard drive size")
def impl_step(context):
    context.speed = 7200
    context.hdd_size = 500

@when("a city is inputted")
def impl_step(context):
    context.city = City("ABC", (0,0), 56)

@then("show difference in time between network and HDD")
def impl_step(context):
    response = context.city.time_diff(context.speed, context.hdd_size)
    assert response == 10

