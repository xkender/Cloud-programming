

"""

abc = a**3 + b**3 + c**1


    # armstrong numbers
    # 125 = 1**3 + 2**3 + 5**3
    # only for 3digit numbers
    # 4 tane var

    # 17 // 10 = 1
    # 17 % 10 = 7

"""

def get_digits(i):
    """
    return digits of a 3-digit number
    :param i: 3-digit number
    :return: a tuple of h, t, u
    """
    h = i // 100
    u = i % 10
    t = (i - h*100) // 10
    return h, t, u


def print_arms():
    for i in range(100, 1000):
        h, t, u = get_digits(i)
        if h**3 + t**3 + u**3 == i :
            print(" this is an Armstrong number ", i)

#e563c164-45ee-4f7c-887c-d39c73061626
