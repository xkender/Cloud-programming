#Python Crash Course exercises - Page 131 to 145

# Making a list and assigning it to variable withing a range of numbers:
even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 11, 2))
#Using assert to verify/compare the values in lists.
assert even_numbers[2] != odd_numbers[2], "Unexpected"
assert even_numbers[0] != odd_numbers[0], "Unexpected"
assert len(even_numbers) == len(odd_numbers), "Seriously????"
print(odd_numbers)

#Creating an empty list and appending a range of number with a for loop.
new_list = []
for value in range(1, 32, 2):
    new_list.append(value**2)
    #print(new_list)
print(new_list)

#Using min, max, sum functions for list value calculations, statistics
print(min(new_list))
print(max(new_list))
print(sum(new_list))

#Using List comprehensions! This allows to write above code in just a line
new_list1 = [value**2 for value in range(1,11)] #No colon is used after for loop!
print(new_list1)

million_numbers = [value+23-3*3/2+12 for value in range(1, 10)]
print(million_numbers)

#creating a dictionary with multiple line usage
user_0 = {
    'username': 'isko',
    'password': '1231',
    'first': 'iskender',
    'last': 'sahin',
    }

#using a for loop to print items of the dictionary
for key, value in user_0.items():
    print("\nKey: ", key)
    print("Value: " + value)


#Creating an emtpy dictionary and then adding items to it
team_support = {}
team_support['iskender'] = 'fenerbahce'
team_support['firat'] = 'galatasaray'
team_support['kivanc'] = 'besiktas'
team_support['eser'] = 'trabzon'

#printing to see the final version of the dictionary and using assert to verify
print(team_support)
assert team_support['eser'] == "trabzon", "Error"


#modifying a value in dictionary
team_support['eser'] = 'karabukspor'
print(team_support)

#creating new dictionary for team and score
game_x = {'fenerbahce': 0, 'galatasaray': 0}

#modifying a value in dictionary
game_x['fenerbahce'] = 5

#printing the final version of the dictionary
print(game_x)

#creating function with a if-elif-else condition for using 2 dictionaries for game outcome
def game_winner():
    if game_x['fenerbahce'] > game_x['galatasaray']:
        print("Winner is: ", team_support['iskender'])
    elif game_x['fenerbahce'] < game_x['galatasaray']:
        print("Winner is: ", team_support['firat'])
    else:
        print("Final score is a draw between", team_support['firat'], "and", team_support['iskender'])
#modifying game_x dictionary to change score to see alternative conditions
game_x['galatasaray'] = 4
#calling the game_winner function
game_winner()



#removing a key-value from dictionary
#del removes the key value pair from the dictionary permanently
print("Original dictionary: ", team_support)
del team_support['eser']
print("Removing eser: karabukspor from the team_support dictionary")
print("Modified dictionary: ", team_support)
