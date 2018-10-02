
class Restaurant():
    """Creating a class named Restaurant with 2 attributes"""

    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name #instance variable
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_name)

    def open_restaurant(self):
        print(self.restaurant_name + "-" +self.cuisine_name + " is open" )

restaurant = Restaurant("Nizam", "Mediteranian Cuisine") #making an instance from class

print(restaurant.restaurant_name)
print(restaurant.cuisine_name)

restaurant.describe_restaurant() #calling the method
restaurant.open_restaurant()
#print(restaurant.describe_restaurant)
#print(restaurant.open_resturant)
