

def double(k):
    i = 4
    return 2*k

def my_add(i, j):
    k = 3
    i = double(i) + j
    print("inside the function ", i)
    return i

x = 6
result = my_add(x, 4)
print(result)
print(x)
print("\n")

#

def increase(x):
    x = 1 + x

x = 5
increase(x)
print(x)
print()



def my_append(l, j):
    l.append(j)

l1 = [1, 2, 3, 5, 6, 8, 9]
print(l1)
my_append(l1, 4)
print(l1)

x = int("5")
print (x + 1 )

x= "a"
while not x.isdigit():
    x = input("enter a number ")
    if x.isdigit() :
        x = int(x)
        break

print(x +1 )
