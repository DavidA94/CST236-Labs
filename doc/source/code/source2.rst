Source Example
==============

Source2 provides functions for describing a polygon.

Determining Polygon Type
^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source1.get_poly_type` provides users with a way to provide a set of four sides
of a polygon and returns the type of polygon ("square", "rectangle", or "invalid") or provides users with 
a way to provide a set of four angles and returns whether the polygon is a "square", "rhombus", or "disconnected"

Rectangle Example
^^^^^^^^^^^^^^^^^

>>> from source.source2 import get_poly_type
>>> get_poly_type(1, 2, 1, 2)
'rectangle'

Rhombus Example
^^^^^^^^^^^^^^^

>>> from source.source2 import get_poly_type
>>> get_poly_type(135, 45, 135, 45, True)
'rhombus'

Complex Documentation
^^^^^^^^^^^^^^^^^^^^^

.. testsetup:: *
    
    from source.source2 import get_poly_type
    a = 1
    b = 2
    c = 1
    d = 2

.. doctest::

    >>> get_poly_type(a, b, c, d)
    'rectangle'
    
.. testcode:: rectangle
    
    print get_poly_type(a, b, c, d)
    
.. testoutput:: rectangle
    
    rectangle

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source2
    :members: