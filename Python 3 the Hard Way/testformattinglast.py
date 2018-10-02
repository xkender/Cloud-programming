
"""
number = [ (x + y + z) for x in range(1,10) for y in range(0,10) for z in range(0,10) ]
print(number)
print("Part1")
print()
"""

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
        #print("{}**{}= {}".format(i, l, a), "{}**{}= {}".format(j, l, b), "{}**{}= {}".format(x, l, c))
print()
threesum.sort()
print(threesum, end=' ')

numberx = list(range(100,1000))
print(numberx)
print("Part2")
print()

equals = list(set(threesum).intersection(set(numberx)))
print()
print(equals)







"""
for i in range(3):
    for i in range(3,10):
        number = i**3 + i**3 + i**3
"""



"""
list1 = list(range(1,10))
print(list1)

list2 = list(range(0,10))
print(list2)

list3 = list(range(0,10))
print(list3)

numberlist = "{}{}{}".format(list1, list2, list3)
print(numberlist)
print()
print()
print()

"""

#while number == list1:
#    print(number, end='')

#numberx = sorted(i**3 + (i+1**3) + (i+2)**3) for i in range(10))
#print(numberx)

#print(number)
#xyz = (number.format(x, y, z) for x in list1 for y in list2 for z in list3)
#xyz = list[xyz]
#print(xyz)






#number = [*map(int, number)]





"""
for i in number:
    if i == (i**3) + (i**3) + (i**3)
        print(i)
"""




"""
a = [value**3 for value in range(1,11)]
print(a)

b = [value**3 for value in range(1,11)]
print(b)

c = [value**3 for value in range(1,11)]
print(c)
"""




"""
a = [x**3 for value in range(1,10)]
print(a)
"""

#[(x,y,z) for x in range(1,10) for y in range(x,10) for z in range(y,10) if value == x**3 + y**3 + z**3]





"""
for x in range(1, 10):
    print(x)

x = [x**3 for value in range(1,10)]
print(x)

xyz = int(xyz)
x = [x**3 for value in range(1,10)]
print(x)

y = [y**3 for value in range(0,10)]
print(y)

z = [z**3 for value in range(0,10)]
print(z)
"""







"""
for x in range(1, 10)

for y in range(0,10)

for z in range(0.10)
"""




"""
for i in range(1, 10):
        a = i

for i in range(1, 2):
    for j in range(2):
        for k in range(2):
        #a = int("{}{}{}".format(i, j, k))
            print()
            b = (i**3 + j**3 + k**3)



print(a, end=" ")
print(b, end=" ")

if a == b:
    print("Three digit Armostrong Numbers are: {} ".format(a))
else:
    print("Nothing here")


if xyz == (x**3 + y**3 + z**3):
    print("{}")
"""
