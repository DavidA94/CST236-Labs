Car Documentation
=================

Car provides the ability to store a speed and make in one object. If given a predefined make (Porsche, Bus, Cement Truck, or laden swallow),
and no speed, then the speed will be automatically set. Other types default to 55.

Cration Speed Examples
^^^^^^^^^^^^^^^^^^^^^^

>>> from source.Car import Car
>>> car = Car(make='Porsche')
>>> car.speed
100
>>> car = Car(make='Bus')
>>> car.speed
65
>>> car = Car(make='Cement Truck')
>>> car.speed
55
>>> car = Car(make='laden swallow')
>>> car.speed
70
>>> car = Car(make='Other')
>>> car.speed
55
>>> car = Car(make='Other', speed=45)
>>> car.speed
45


Module Reference
^^^^^^^^^^^^^^^^

.. autoclass:: source.Car.Car
   :members: