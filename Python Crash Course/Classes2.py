class Car():
    """Creating a class for Cars"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted get_descriptive_name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car's milage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer_reading to the given value
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Car('bmw', 'x5', 2017)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Modifying attribute values
#Modifying directly:
my_new_car.odometer_reading = 23
my_new_car.read_odometer()



#-----------------
#Modifying attribute value through a method: Added below code to inside class
#def update_odometer(self, mileage):
#    """Set the odometer_reading to the given value"""
#    self.odometer_reading = mileage

my_new_car.update_odometer(230)
my_new_car.read_odometer()
#-----------------

#-----------------
#Added below if-else logic code to update_odometer method to prevent odometeroll back

#if mileage >= self.odometer_reading:
#    self.odometer_reading = mileage
#else:
#    print("You can't roll back an odometer!")

my_new_car.update_odometer(20)
my_new_car.read_odometer()
#----------------

#-----------------
#Incrementing an attribute's value through a method:
#Added below method to class above...
#def increment_odometer(self, miles):
#    """Add the given amount to the odometer reading."""
#    self.odometer_reading += miles

my_used_car = Car('kia', 'sedona', '2016')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


class ElectricCar(Car):
    """Represent aspects if a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery_size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
