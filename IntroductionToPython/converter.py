"""
Notes:
Python Programming: (Python 3)
An introduction to Computer Science:

Pseudocode: Precise English that describes what a program does:

Input the temperature in degrees Celsius
Calculate fahrenheit as (9/5)celsius + 32
Output fahrenheit

Concatenation: combining strings using addition: (Gluing the strings together)
>>>"Bat" + "man"
'Batman'

Garbage collection: old variable values (assignments are used to assign new values) are erased by  Python automatically (automatic memory management).

"""

#F_to_C_Converter.py
#A program to conver celsius temps to fahrenheit
#by: isko

def main():
    celsius = eval(input("What is the Celsius temperature?")) #talk about "eval" with Tolga. What if user enters text instead of a number?
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees fahrenheit.")

#In the first run I did not close the function with main() so nothing happened when I ran the file in python.

main()

def reverse():
    fahrenheit = eval(input("What is the fahrenheit temperature?"))
    celsius = (fahrenheit - 32) * (5/9)
    print("The temperature is", celsius, "degrees" + " celsius") #Concatenation

reverse()

#Questions to Tolga: "How to round the outcome", "how to use a variable value in another function"
