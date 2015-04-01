"""
:mod:`source.source2` -- New source code
============================================

The following code determines if four given sides create a square, a rectangle,
or something else.
"""

def get_poly_type(a=0, b=0, c=0, d=0, angles=False):
    """
    Determine if the given polygon is square, rectangle, rhombus, or other

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float or int

    :param c: line c
    :type c: float or int

    :param d: line d
    :type d: float or int

    :param angles: True if given angles
    :type angles: bool

    :return: "square", "rectangle", "rhombus" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 4:
        keys = []
        for key in a.keys():
            keys.append(key)
            
        keys.sort()
        d = a[keys[3]]
        c = a[keys[2]]
        b = a[keys[1]]
        a = a[keys[0]]

    if not (isinstance(a, (int, float)) and
            isinstance(b, (int, float)) and
            isinstance(c, (int, float)) and
            isinstance(c, (int, float))):
        return "invalid"

    if angles:
        if (a + b + c + d) % 360 != 0:
            return "disconnected"

        if (a != 90 and b != 90 and
            c != 90 and d != 90):
                return "rhombus"

        elif (a == 90 and b == 90 and
              c == 90 and d == 90):
            return "square"

        else:
            return "disconnected"

    else:
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            return "invalid"
        
        if ((a == b) and (b == c) and
            (c == d) and (d == a)):
                return "square"

        elif ((a == c) and (b == d)):
            return "rectangle"

        else:
            return "invalid"
            
