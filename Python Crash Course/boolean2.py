

car = "BMW"

print(car == "BMW", car == "Honda", car == "Bmw")


def ticket(age):
    if age < 4:
        price = 0

    elif age < 18:
        price = 5

    elif age > 65:
        price = 1

    else:
        price = 10

    print("Ticket price is " + str(price) + " USD") # QUESTION: Any difference using "," or "+" ?

    print("Your ticket price is", price, "USD")

ticket(70)


"""
Testing Multiple Conditions:

The if-elif-else chain is powerful, but it’s only appropriate to use when you
just need one test to pass. As soon as Python finds one test that passes, it
skips the rest of the tests. This behavior is beneficial, because it’s efficient
and allows you to test for one specific condition.
However, sometimes it’s important to check all of the conditions of interest.
In this case, you should use a series of simple if statements with no elif or
else blocks. This technique makes sense when more than one condition could be
True, and you want to act on every condition that is True.
"""



numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print("These are all great numbers, check each one out: ", number )

print("Nice, now you know all the numbers in the numbers list")


drinks = ['cola', 'fanta', 'ayran']

for drink in drinks:
    if drink == 'ayran':
        print("\nKusura bakmayin " + drink + "imiz kalmadi :( ")
    else:
        print("\nBuyrun efendim iceceginiz :) ", drink)
