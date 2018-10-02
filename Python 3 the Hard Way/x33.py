def whileloop(j, k):

    i = 0
    numbers = []

    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + k
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

whileloop(1150, 2)
