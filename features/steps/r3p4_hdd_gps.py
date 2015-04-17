from behave import *
from source.Cities import Cities
from source.hdd import HDD

@given("An HDD")
def impl_step(context):
    context.HDD = HDD(100, 1)
    context.cities = Cities()

@then("Require a G/s")
def impl_step(context):
    assert context.HDD.gps == 1
    assert context.HDD.size == 100


@when("Updating the G/s")
def impl_step(context):
    context.cities.change_hdd_gps(2)


@then("Update the G/s")
def impl_step(context):
    assert context.cities.hdd.gps == 2
