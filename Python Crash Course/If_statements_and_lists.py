pizza_toppings = ["mushrooms", "tomato", "salami", "cheddar", "mozeralla", "olives"]
requested_toppings = ["tomato", "cheddar", "beyaz_peynir"]


for requested_topping in requested_toppings:
    if requested_topping in pizza_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("Your pizza is ready!")
