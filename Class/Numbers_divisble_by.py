

# 1000 - 2000 arasinda 7 ve 11 e bolunebilen yada sadece 13 e bolunebilen sayilari bul


def divisible_by_7_and_11_or_13(i):

    if i % 7 == 0 and i % 11 == 0:
        return True
        print(i, "is disivible by 7 and 11")
    return False

    if i % 13 == 0:
        return True
        print(i, "is divisible by 13")
    

assert(divisible_by_7_and_11_or_13(1925))  # QUESTION: How do you user assert for IF else or IF IF conditions?
assert(divisible_by_7_and_11_or_13(1848))
assert(not divisible_by_7_and_11_or_13(1200))

def numbers_x_to_y(x,y):
    for j in range(x,y):
        divisible_by_7_and_11_or_13(j)


#numbers_x_to_y(1000,2000)



"""
assert(divisible_by_7_and_11_or_13(22))
assert(divisible_by_7_and_11_or_13(77))
assert(not divisible_by_7_and_11_or_13(34))
assert(not divisible_by_7_and_11_or_13(14))
"""

"""
    elif i % 13 == 0:
        return True
        print(i)
"""
