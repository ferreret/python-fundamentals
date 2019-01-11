"""
A module for demostrating exceptions
"""
import sys
from math import log


def convert(s):
    """
    Convert to an integer
    :param s:
    :return:
    """
    try:
        return int(s)
        # print("Conversion succeded! x =", x)
    except (ValueError, TypeError) as e:
        # print("Conversion failed!")
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise


def string_log(s):
    """
    Do de log of the param
    :param s:
    :return:
    """
    v = convert(s)
    return log(v)


# res = convert("hola")
# print(res)
# res = convert("124")
# print(res)
# res = convert([4, 5, 6])
# print(res)

string_log([1, 2, 3])
