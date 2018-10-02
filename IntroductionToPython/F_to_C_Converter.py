"""
Notes:
Python Programming: (Python 3)
An introduction to Computer Science:

Pseudocode: Precise English that describes what a program does:

Input the temperature in degrees Celsius
Calculate fahrenheit as (9/5)celsius + 32
Output fahrenheit

"""

#F_to_C_Converter.py
#A program to conver celsius temps to fahrenheit
#by: isko

def main():
    celsius = eval(input("What is the Celsius temperature?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees fahrenheit.")
