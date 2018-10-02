

# 1000 - 2000 arasinda 7 ve 11 e bolunebilen yada sadece 13 e bolunebilen sayilari bul

def my_append(l, j):
    l.append(j)

def divisible_by_7_and_11(i):

    if i % 7 == 0 and i % 11 == 0:
        #print(i, "is disivible by 7 and 11")
        l1 = []
        my_append(l1, i)
        l1a = my_append(l1, i)
        print("Numbers divisible by 7 and 11: ", l1a.count(i))
        return True
    return False



def divisible_by_13(i):

    if i % 13 == 0:
        #print(i, "is divisible by 13")
        #return True QUESTION: return true kullanmaya ihtiyac var mi?
        l2 = []
        my_append(l2, i)
        print("Numbers divisible by 13: ", l2.count(i))
        return True
    return False


def numbers_x_to_y(x,y):
    for j in range(x,y):
        divisible_by_7_and_11(j)
        divisible_by_13(j)



numbers_x_to_y(1000,2000)







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
