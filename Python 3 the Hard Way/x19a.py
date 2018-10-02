#using print(f" ") in a function
def beers_and_crackers(beer_c, crackers_c):
    print(f"\nYou have {beer_c} beers, and {crackers_c} crackers")

beers_and_crackers(10, 20)

#using print(" ".format) in a function
def beers_and_crackers_2(beer_c1, crackers_c1):
    print("You have {} beers, and {} crackers".format(beer_c1, crackers_c1))

beers_and_crackers_2(20, 30)

print("How about some user input?")

beer_count = float(input("How many beers do you need sir?"))
#beer_count = int(beer_count) #Converting user input to integer
#beer_count = int(beer_count) instead use int(input()) or float(input())
crackers_count = int(input("How many crackers do you need?"))
#crackers_count = int(crackers_count)

beers_and_crackers(89-65+beer_count, crackers_count+3)
