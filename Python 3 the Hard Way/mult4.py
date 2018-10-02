"""
print()
print()
print("    10X Multiplication Table ")
print("---------------------------------")

def mult_table(a, b, c):
    print("a", end=" ")
    for i in range(a, b, c):
        print(i, end=" ")
    print()
mult_table()

mult_table(1, 11, 1)
"""


"""
for i in [0, 1, 2, 3]: #counted loop
    print (i, end=' ')
print()
for odd in [1, 3, 5, 7, 9]: # counted loop
    print(odd * odd, end=' ')
"""



print()
print()
print("    10X Multiplication Table ")
print("_________________________________________________________________________________")

for i in range(1, 11):
    print()
    for j in range(1, 11):
        a = (i * (i+1))
        print("{}x{:<1}={:<3}".format(i, j, a), end="")

print()
print("_________________________________________________________________________________")
