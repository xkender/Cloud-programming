print()
print()
print("     ")
print("__________________________________________________________10X Multiplication Table________________________________________________________")

for i in range(1, 10):
    print()
    for j in range(1, 11):
        a = (i * j)
        print("{:>4}x{:<1} = {:<3} ".format(i, j, a), end=" ")
print()
for i in range(10, 11):
    for j in range(1, 11):
        a = (i * j)
        print("{:>4}x{:<2}= {:<3}".format(i, j, a), end="  ")

print()
print("__________________________________________________________________________________________________________________________________________")
