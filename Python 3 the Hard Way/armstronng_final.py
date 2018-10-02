
"""
l = 3
threesum = []
for i in range(1, 10):
    print()
    for j in range(0, 10):
        a = (i**l)
        b = (j**l)
        x = (j+1)
        c = (x**l)
        d = (a + b + c)
        threesum.append(a + b + c)
        print("{}**{}= {}".format(i, l, a), "{}**{}= {}".format(j, l, b), "{}**{}= {}".format(x, l, c))
print()
threesum.sort()
print(threesum, end=' ')
"""

threes = []
for x in range(1,10):
    threes.append(x**3)
print(threes, end=' ')

threes2 = []
for i in threes:
    threes2.append(i + i + i)
print(threes2)
print()
print()

"""
threes3 = [x + y + z for x in [1,2,3,4,5,6,7,8,9] for y in [1,2,3,4,5,6,7,8,9] for z in [1,2,3,4,5,6,7,8,9]]
threes3.sort()
print(threes3)
print()
"""

"""
from itertools import combinations
lis = [1,2,3,4,5,6,7,8,9]
for i in range(1, len(lis) + 1):
    for comb in combinations(lis, i):
       if sum(comb) == 153:
           print(comb)
"""


numberx = list(range(100,1000))
print(numberx)
print("Part2")
print()

equals = list(set(threes2).intersection(set(numberx)))
print()
equals.sort()
print(equals)
