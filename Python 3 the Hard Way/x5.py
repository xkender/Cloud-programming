my_name = 'Iskender Sahin'
my_age = 40 #Getting old :))
my_height = 68 #inches
my_weight = 190 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.") #using f and {} characters to locate variables in a string is called "format string".
print(f"Let's talk about {my_hair} with {my_name}")
my_hair = "Black"
pattern = "Let's talk about {} with {}"
print(pattern.format(my_hair, my_name))
my_hair ="Blonde"
my_name="tolga"
print(pattern.format(my_hair, my_name))


print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's nost too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it it exactly right!!
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_weight}, and {my_weight} I get {total}.")

a = "freedom"
b = "of"
c = 8 + 14
practice = "It is a modern way of using Python {}, {}, {}"
print(practice.format(a, b, c))
