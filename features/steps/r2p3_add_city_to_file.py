import os
from behave import *
from source.Cities import Cities
from source.City import City

@given("A new city")
def impl_step(context):
    context.cities = Cities()
    context.cities.add_city(City("Wilsonville", (10, 50), 56))

@then("Append that city to the cities file")
def impl_step(context):
    f = open(context.cities.filename, 'r')
    assert f.read() == "Wilsonville, (10,50), 56\n"
    f.close()
    os.remove(f.name)

@given("A city to be removed")
def impl_step(context):
    context.cities = Cities()
    context.cities.add_city(City("Wilsonville", (10, 50), 56))
    context.cities.add_city(City("Portland", (30, 45), 100))
    context.rem_city = City("Wilsonville", (10, 50), 56)

@then("Remove city and update file")
def impl_step(context):
    f = open(context.cities.filename, 'r')
    assert f.read() == "Wilsonville, (10,50), 56\nPortland, (30,45), 100\n"

    context.cities.rem_city(context.rem_city)
    f.seek(0)
    assert f.read() == "Portland, (30,45), 100\n"

    f.close()
    os.remove(f.name)
