#Excerpt From: Eric Matthes. “Python Crash Course.” iBooks.
#Chapter 7 - Using a while Loop with Lists and dictionaries
#Page 250

"""
“A for loop is effective for looping through a list, but you shouldn’t modify a
list inside a for loop because Python will have trouble keeping track of the
items in the list. To modify a list as you work through it, use a while loop.
Using while loops with lists and dictionaries allows you to collect, store, and
organize lots of input to examine and report on later.”
"""


#start with users that need to be verified
#and an empty list to hold confirmed users

print("\nconfirmed_users.py: \n")
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

#verify each user until no unconfirmed
#move each verfied user to the confirmed user list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

#Display all confirmed users
print("\nThe following users have been confirmed")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#Removing All Instances of Specific Values from a List ()
#Say you have a list of pets with the value 'cat' repeated several times.
#To remove all instances of that value, you can run a while loop until 'cat'
#is no longer in the list, as shown here:


print("\npets.py: \n")
pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# tried using and in a while loop in below scenario
"""
print("\npets.py: \n")
pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' and 'dog' in pets:
    pets.remove('dog')
    pets.remove('cat')

print(pets)
"""

#Filling a Dictionary with User Input:
#You can prompt for as much input as you need in each pass through a while
#loop. Let’s make a polling program in which each pass through the loop prompts
#for the participant’s name and response. We’ll store the data we gather in a
#dictionary, because we want to connect each response with a particular user:


print("\nmountain_poll.py: \n")

responses = {}

#Set a flag to indicate that polling is actuveselfself.
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #Store the response in the Dictionary
    responses[name] = response
    #Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
