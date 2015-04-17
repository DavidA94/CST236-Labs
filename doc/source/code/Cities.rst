Cities Documentation
====================

Cities is an all inclusive class that allows for calculating speeds between cities with a network or an HDD.

Cities Creation
^^^^^^^^^^^^^^^

>>> from source.Cities import Cities
>>> from source.City import City
>>> cities = Cities(filename='cities.txt', start_city=City("Wilsonville", (10, 40), 56))


Module Reference
^^^^^^^^^^^^^^^^

.. autoclass:: source.Cities.Cities
   :members: