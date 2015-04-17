from behave import *
from source.City import City
from source.hdd import HDD

@given("a speed and hard drive size")
def impl_step(context):
    context.hdd = HDD(500, 1)

@when("a city is inputted")
def impl_step(context):
    context.city = City("ABC", (0,0), 56)

@then("show difference in time between network and HDD")
def impl_step(context):
    response = context.city.time_diff(context.hdd)
    assert response == 10

