
#number = 153

#test = sum((x,y,z) for x in range(1,10) for y in range(0,10) for z in range(0,10) x**3 + y**4 + z**2)

#print(test)

#[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]



# [(x,y,z) for x in range(1,10) for y in range(x,10) for z in range(y,10) if value == x**3 + y**3 + z**3]

threesum = []

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
x = (x**3 for x in range(10))
x = list(x)
print(x)
"""






"""
for i in range (1, 10):
    a = (i**3)
    print(a)
for j in range (0, 10):
    b = (j**3)
for k in range (0, 10):
    c = (k**3)

d = a + b + c
print(d)
"""
