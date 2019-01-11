import  sys

def sqrt(x):
    """
    Compute square roots using the method of Heron of Alexandria
    :param x:
        The number for which the square root is to be computed.
    :return:
        The square root of x
    """
    guess = x
    i = 0

    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))

    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(str(e), file=sys.stderr)


if __name__ == "__main__":
    main()
