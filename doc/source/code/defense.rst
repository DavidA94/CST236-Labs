Shield Example
===============

Defence provides a defence for fighting orcs

Determining if the Defence is safe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.defense.Shield.is_safe` allows a user to check if their defence is safe or not.

is_safe Example
^^^^^^^^^^^^^^^

>>> from source.defense import Shield
>>> from source.orc import Orc
>>> s = Shield(100)
>>> s.orcs.append(Orc(50))
>>> s.is_safe()
False

The function :func:`source.defense.Shield.perim` gets the perimeter of the defence

perim Example
^^^^^^^^^^^^^

>>> from source.defense import Shield
>>> s = Shield(100)
>>> s.perim()
100


.. note::

    orc_speeds and orc_dists return lists of speeds and distances by looping through the orcs
    and getting their speeds and distances from the Orc object.


Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.defense
    :members:
