print()
print()
print("     ")
print("______________________10X Multiplication Table______________________")

for i in range(1, 10):
    print()
    for j in range(1, 6):
        a = (j * i)
        print("{:>4}x{:2} = {:3} ".format(j, i, a), end=" ")

print()
for i in range(10, 11):
    for j in range(1, 6):
        a = (j * i)
        print("{:>4}x{:2} = {:3}".format(j, i, a), end="  ")

print()
for i in range(1, 10):
    print()
    for j in range(6, 11):
        a = (j * i)
        print("{:>4}x{:2} = {:3} ".format(j, i, a), end=" ")

print()
for i in range(10, 11):
    for j in range(6, 11):
        a = (j * i)
        print("{:>4}x{:2} = {:3}".format(j, i, a), end="  ")

print()
print("____________________________________________________________________")
