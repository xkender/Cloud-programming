
def describe_pet(animal_type, pet_name):
    """Displaying information about an animal and animal name"""
    print("Animal's type: " + animal_type.title() + "\nAnimal's name: " + pet_name.title() + ".")


describe_pet('kedi', 'kihiro') #positional argument to call a function
describe_pet('inek', 'rudolfo') #positional argument to call a function
describe_pet(animal_type='dinazor', pet_name='rara') #keyword argument to call a function
describe_pet(pet_name='rara', animal_type='dinazor') #keyword argument to call a function

#Default Values:

"""When writing a function, you can define a default value for each parameter.
If an argument for a parameter is provided in the function call, Python uses the
argument value. If not, it uses the parameter’s default value.”
Excerpt From: Eric Matthes. “Python Crash Course.” iBooks."""

def describe_pet_2(pet_name, animal_type='dog'):
    """Displaying information about an animal and animal name"""
    print(animal_type.title() + "'s name: " + pet_name.title() + ".")


#describe_pet_2(pet_name='roxy')
#Note that if animal type was the first argument this would give an error
#When one argumenet does not have default value it is a positional argument
#So you have to call the function with correct order or just the name like below:
describe_pet_2('roxy')
describe_pet_2(pet_name='rara', animal_type='dinazor')

""" NOTE:
“When you use default values, any parameter with a default value needs to be
listed after all the parameters that don’t have default values. This allows
Python to continue interpreting positional arguments correctly.”
"""


#Return Values:
"""
“A function doesn’t always have to display its output directly. Instead, it can
process some data and then return a value or set of values. The value the
function returns is called a return value. The return statement takes a value
from inside a function and sends it back to the line that called the function.
Return values allow you to move much of your program’s grunt work into functions,
which can simplify the body of your program.”
"""

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name

musician = get_formatted_name('Eric', 'Clapton')
print(musician)


def get_formatted_name_2(first_name, last_name, middle_name='' ):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' +last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name_2('Jimi', 'Hendrix')
print(musician)
musician = get_formatted_name_2('John', 'Hooker', 'Lee')
print(musician)

"""# NOTE:
“Calling above function with a first and last name is straightforward. If we’re
using a middle name, however, we have to make sure the middle name is the last
argument passed so Python will match up the positional arguments correctly”
"""

#RETURNING A Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('Fazil', 'Say')
print(musician)


def build_person_2(first_name, last_name, age=''):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person_2('Jimi', 'Hendrix', age=27)
print(musician)


#USING A FUNCTION WITH A WHILE Loop
def get_formatted_name_3(first_name, last_name):
    """Return a full name, neatly formatted, use while loop"""
    

    #This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

formatted_name = get_formatted_name_3(f_name, l_name)
print("\nHello, " + formatted_name + "!")
