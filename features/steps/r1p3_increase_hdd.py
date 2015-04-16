from behave import *
from source.Cities import Cities

@given("I'm researching speeds with little space")
def step_impl(context):
    context.cities = Cities()

@when("more space is needed")
def step_impl(context):
    context.more_space = 100

@then("increase HDD size")
def step_impl(context):
    context.cities.add_hdd_space(100)
    assert context.cities.hdd_space == 200