

# 1000 - 2000 arasinda 7 ve 11 e bolunebilen yada sadece 13 e bolunebilen sayilari bul


def divisible_by(k, s, l, v, w):

    list1 = []
    for i in range(v, w):
        if i % k == 0 and i % s == 0:
            list1.append(i)
    print()
    print("Between {} and {}, there are".format(v, w), len(list1),"numbers divisible by {} and {}: ".format(k, s), list1)
    print()

    list2 = []
    for j in range(v, w):
        if j % l == 0:
            list2.append(j)
    print("Between {} and {}, there are".format(v, w), len(list2), "numbers divisible by {}: ".format(l), list2)
    print()


divisible_by(7, 11, 13, 1000, 2000)














"""
def my_append(l, j):
    l.append(j)
"""



"""
l1 = []
my_append(l1, i)
l1a = my_append(l1, i)
print("Numbers divisible by 7 and 11: ", l1a.count(i))
"""


"""
for i in [0, 1, 2, 3]:
    print (i)
"""

"""
a = []
for i in range(5):
    a.append(i)
print(a)
"""
