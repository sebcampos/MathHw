# These functions taken from Geeks4Geeks

def gcd(a, b):
    """
    This method finds the greatest common denominator
    :param a: int or float
    :param b: int of float
    :return: float
    """
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    """
    This method returns the least common denominator
    :param a:  int or float
    :param b:  int or float
    :return: float
    """
    return (a * b) / gcd(a, b)
