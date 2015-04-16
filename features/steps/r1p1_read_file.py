from behave import *
from source.Cities import Cities
from source.City import City
from testfixtures import LogCapture
import os

@given("I'm researching speeds")
def step_impl(context):
    context.log = LogCapture()
    context.cities = Cities()


@when("given a file")
def step_impl(context):
    context.f = open("ABC_TEMP.txt", 'w+')
    f = context.f
    f.write("Wilsonville, (10,50), 56\n")
    f.write("Portland, (30,45), 100\n")
    f.write("Lake Oswego, (20,60), 65\n")
    f.write("Woodburn, (-10,40), 65\n")
    f.flush()
    f.seek(0)


@then("read in data")
def step_impl(context):
    context.cities.read_from_file(context.f)
    test_con = [City("Wilsonville", (10, 50), 56),
                City("Portland", (30, 45), 100),
                City("Lake Oswego", (20, 60), 65),
                City("Woodburn", (-10, 40), 65)
    ]

    assert context.cities.cities == test_con

    context.log.check(("cities_log", "INFO", "Creating new cities object"),
                      ("city_log", "INFO", "New City Created"),
                      ("cities_log", "INFO", "Adding city: Wilsonville -- Location: (10, 50); C_Speed: 56"),
                      ("city_log", "INFO", "New City Created"),
                      ("cities_log", "INFO", "Adding city: Portland -- Location: (30, 45); C_Speed: 100"),
                      ("city_log", "INFO", "New City Created"),
                      ("cities_log", "INFO", "Adding city: Lake Oswego -- Location: (20, 60); C_Speed: 65"),
                      ("city_log", "INFO", "New City Created"),
                      ("cities_log", "INFO", "Adding city: Woodburn -- Location: (-10, 40); C_Speed: 65"),
                      ("city_log", "INFO", "New City Created"),
                      ("city_log", "INFO", "New City Created"),
                      ("city_log", "INFO", "New City Created"),
                      ("city_log", "INFO", "New City Created")
    )

    context.log.uninstall()
    context.f.close()
    os.remove(context.f.name)

@when("making a bad city")
def impl_step(context):
    context.city1 = City(123, (1,2), 10)  # Not str
    context.city2 = City("ABC", 1, 10)  # Not tuple
    context.city3 = City("ABC", (1, 2), 'a')  # Not int

@then("make city attributes None and log error")
def impl_step(context):
    assert (context.city1.name is context.city1.location is context.city1.connection_speed ==
            context.city2.name is context.city2.location is context.city2.connection_speed ==
            context.city3.name is context.city3.location is context.city3.connection_speed is None)

    context.log.check(("cities_log", "INFO", "Creating new cities object"),
                      ("city_log", "ERROR", "Bad attribute type passed in."),
                      ("city_log", "ERROR", "Bad attribute type passed in."),
                      ("city_log", "ERROR", "Bad attribute type passed in.")
                      )

    context.log.uninstall()


@when("adding a bad city")
def impl_step(context):
    context.cities.add_city(None)

@then("put error in log and don't add")
def impl_step(context):
    context.log.check(("cities_log", "INFO", "Creating new cities object"),
                      ("cities_log", "ERROR", "Attribute city must be of type City"),
                      )

    context.log.uninstall()

@when("wanting to remove a city")
def impl_step(context):
    context.cities.add_city(City("A", (0,0), 56))
    context.rem_city = City("A", (0,0), 56)

@then("remove city")
def impl_step(context):
    context.cities.rem_city(context.rem_city)

    assert len(context.cities.cities) == 0
    context.log.uninstall()

@when("wanting to remove a bad city")
def impl_step(context):
    pass

@then("put error in log and don't remove anything")
def impl_step(context):
    context.cities.rem_city('a')

    context.log.check(("cities_log", "INFO", "Creating new cities object"),
                      ("cities_log", "ERROR", "Attribute city must be of type City"),
                      )

    context.log.uninstall()