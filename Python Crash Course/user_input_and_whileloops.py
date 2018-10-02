#Excerpt From: Eric Matthes. “Python Crash Course.” iBooks.
#Chapter 7 - User Input and While Loops

#using input for user input
number = input("Enter a number, and I'll tell if it is even or odd: ")
#using int to convert user input to integer which is by default string
number = int(number)
#using the Modulo operator with if-else to distinguish odd/even numbers
#by dividing the numbers by 2 and check if that equals to zero or not
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")


'''
“The for loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or while, a certain condition is true.”
Excerpt From: Eric Matthes. “Python Crash Course.” iBooks.
'''

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program.."
message = "" #giving reference value to message variable for python
#to not give an error when it reads message in while loop
while message != 'quit':
    message = input(prompt)
#added if statement to prevent printing 'quit' even after user types quit to quit
    if message != 'quit':
        print(message)


"""
FLAGS: Page 253
“For a program that should run only as long as many conditions are true, you
can define one variable that determines whether or not the entire program is
active. This variable, called a flag, acts as a signal to the program. ”

“Let’s add a flag to parrot.py from the previous section. This flag, which
we’ll call active (though you can call it anything), will monitor whether or
not the program should continue running:”
"""


prompt = "\nTell me something, and I will repeat it back to you!, No?:"
prompt += "\nEnter 'quit' to end the program. "

active = True #Using True flag for while loop to keep running until False
while active:
    message = input(prompt)

    if message == 'quit':
        active = False #setting the flag false which ends the loop
    else:
        print(message)


#Using break statement to end a piece of code running

prompt = '\nCity you visited?'
prompt += 'Enter quit when to quit! :) '

while True:
    city = input(prompt)

    if city == 'quit':
        break #if user inputs "quit" break statement ends the while loop.
    else:
        print("It is a lovely city", city.title())
        #if user does not use 'quit' else condition is used


#Using continue in a loop to skip that condition only and move to next:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
