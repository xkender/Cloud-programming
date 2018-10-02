
def factoriallist(number):

#    list1 = []
    factbase = 1
    for i in range(1, number+1):
        factbase *= i
#        if i >= 1:
#            list1.append(i)
#    print(list1)
#    for f in list1:
#        factbase *= f
    return factbase

# 5! = 5x4x3x2x1
print( factoriallist(1005) )
#factoriallist(1005)




list2 = [1, 2, 3]

print(list2)
print(type(list2))

print(range(1, 4))
print(type(range(1, 4)))
