from behave import *
from source.Car import Car


@given("a new car")
def impl_step(context):
    pass


@when("given a preset car make and no speed")
def impl_step(context):
    context.carP = Car(make='Porsche')
    context.carB = Car(make='Bus')
    context.carC = Car(make='Cement Truck')
    context.carL = Car(make='laden swallow')
    context.carF = Car(make='Ford')


@then("set speed to preset")
def impl_step(context):
    assert context.carP.make == "Porsche" and context.carP.speed == 100
    assert context.carB.make == "Bus" and context.carB.speed == 65
    assert context.carC.make == "Cement Truck" and context.carC.speed == 55
    assert context.carL.make == "laden swallow" and context.carL.speed == 70
    assert context.carF.make == "Ford" and context.carF.speed == 55


@when("given a preset car make and a speed")
def impl_step(context):
    context.carPs = Car(make='Porsche', speed=120)
    context.carBs = Car(make='Bus', speed=55)
    context.carCs = Car(make='Cement Truck', speed=75)
    context.carLs = Car(make='laden swallow', speed=99)
    context.carFs = Car(make='Ford', speed=110)


@then("set speed to passed speed")
def impl_step(context):
    assert context.carPs.make == "Porsche" and context.carPs.speed == 120
    assert context.carBs.make == "Bus" and context.carBs.speed == 55
    assert context.carCs.make == "Cement Truck" and context.carCs.speed == 75
    assert context.carLs.make == "laden swallow" and context.carLs.speed == 99
    assert context.carFs.make == "Ford" and context.carFs.speed == 110
