

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print("Original x-position: " + str(alien_0['x_position']))

#Movie alien to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien :)
    x_increment = 3

#The new position of the alien will be original plus the x_increment.

alien_0['x_position'] += x_increment  # Used += to shortcut adding itself to the x_increment.
print("New x-position: " +  str(alien_0['x_position']))

print(alien_0)
del alien_0['speed'] #removing a value from dictionary >> deleted key value is removed permanently.
print(alien_0)

alien_0['speed'] = 5 #adding a valie to the dictionary
print(alien_0)


#favorites.py

favorite_languages = {     # Showing using multiple lines to print a dictionary
    'ozlem': 'french',
    'iskender': 'english',
    'nese': 'turkce',
    'ozan': 'english',
    }

print("Ozlem's favorite language is " +    #Multiple lines to print multiple items
    favorite_languages['ozlem'].title() +
    ".")
print()
print("Iskender's favorite language is " + favorite_languages['iskender'].title())
print()

for name, language in favorite_languages.items():
    print(name.title() + " " + language.title())

print("\nWith using .keys:")
for name in favorite_languages.keys():
    print(name.title())

print("\nWithout using .keys():")    # Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote ...
for name in favorite_languages:   #You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.
    print(name.title())

print()

friends = ['iskender', 'ozlem']
for name in favorite_languages.keys():
    if name in friends:
        print(name + ": Oh! So, your fav lang is: " +
            favorite_languages[name])
    else:
        print(" ")

if 'Osman' not in favorite_languages.keys():
    print("Osman you should totally take the poll and tell your fav lang!")
print()

for name in sorted(favorite_languages.keys()): #sorting the keys of the dictionary in alphetical order
    print(name, ": using sorted() Your names are sorted! Well done! :)")
print()

for language in favorite_languages.values():
    print(language + ": Using .values() printing the languages in a dictionary " )
print()

"""
As shown below:
When you wrap set() around a list that contains duplicate items,
Python identifies the unique items in the list and builds a set from those items.
"""

for language in set(favorite_languages.values()):
    print(language, ": Using set operator to get rid of repetitive data")
print()


# page 235: Lists in dictionaries and for loops

favorite_languages_2 = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages_2.items():
    print(name + ":")
    for language in languages:
        print(language)
