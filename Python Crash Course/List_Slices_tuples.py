#Working with parts of a list using slices via :
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[2:4])
print(players[:4])
print(players[2:])

#Looping through a list
for player in players[:3]:
    print(player.title())

#Copying a list using [:] instead of saying a list is equal to another
#This is done to be able to use each list seperately for adding or removing items
#If we just equal a list to another, an item will be added to both lists
my_fruits = ["banana", "apple", "strawberry", "grapes"]
his_fruits = my_fruits[:]
#printing original lists
print("My fruits: ",  my_fruits)
print("His fruits: ", his_fruits)
#appending new fruits to each list
my_fruits.append("watermelon")
his_fruits.append("melon")
#printing new updaates lists
print("My fruits: ",  my_fruits)
print("His fruits: ", his_fruits)

#Tuples: Use paranthesis instead of brackets tuple_1("apples", "bananas")
"""
Sometimes you’ll want to create a list of items that cannot change. Tuples allow
you to do just that. Python refers to values that cannot change as immutable,
and an immutable list is called a tuple.
"""
dimensions = (200, 50, 35, 45)
#Accessing tuple items with their index number.
print(dimensions[0])
print(dimensions[:2])
print(dimensions[:])
print(dimensions[:24])
#below gives an error saying tuple object does not support item assignment

assert dimensions[0] == 200


#Writing over a tuple:
dimensions = (100, 50, 35, 45)
print("New dinmensions: ")
for dimension in dimensions:
    print(dimension)



"""
Python Enhancement Proposal (PEP). One of the oldest PEPs is PEP 8,
which instructs Python programmers on how to style their code.
Indentation (4 characters for each tab)
Line Length (79 characters is standard for code)
PEP8 recommends 72 characters for comments
"""
