from behave import *
from source.City import City
from source.hdd import HDD

@given("a speed and HDD size")
def impl_step(context):
    context.hdd = HDD(500, 1)

@when("inputting a city")
def impl_step(context):
    context.fast_hdd = City("ABC", (0,0), 56)
    context.fast_net = City("DEF", (0,0), 100)

@then("output if the HDD or network is faster")
def impl_step(context):
    response1 = context.fast_hdd.check_hdd(context.hdd)
    response2 = context.fast_net.check_hdd(context.hdd)

    assert response1 == "The HDD is faster"
    assert response2 == "The net is faster"