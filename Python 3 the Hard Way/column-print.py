

for i in range(1, 11):
    print()
    for j in range(1, 11):
        a = (j * i)
        print("{}x{:<1}={:<3}".format(j, i, a), end="")
