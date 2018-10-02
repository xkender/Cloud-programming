"""
Functions to help find 3-digits Armstrong numbers
which are of the form;
    abc = a**3 + b**3 + c**3

"""

def get_digits(i):
    """
    this function returns digits of a 3-digit number
    :param i: a 3 digit number
    :return: the digits for i for a 3 digit ber as tuple (hundreds, tens, unit)
    """
    unit = i % 10
    hundred = i // 100
    ten = (i - hundred*100) // 10
    return hundred, ten, unit


def test_get_digits():
    """
    execute unit tests for get_digits
    """
    assert(get_digits(333) != (0, 0, 0))
    assert(get_digits(333) == (3, 3, 3))
    assert(get_digits(100) == (1, 0, 0))
    assert(get_digits(571) == (5, 7, 1))
    assert(get_digits(0) == (0, 0, 0))
    assert(get_digits(999) == (9, 9, 9))
    print("All unit tests passed")


def print_if_armstrong(start, end):
    """
    prints to standard output the Armstrong numbers
    :param start: range start for Armstrong number search
    :param end: range end
    :return: None
    """
    for i in range(start, end):
        h, t, u = get_digits(i)
        if i == h**3 + t**3 + u**3 :
            print(i)


if __name__ == "__main__":
    # test_get_digits()
    print_if_armstrong(100, 1000)
