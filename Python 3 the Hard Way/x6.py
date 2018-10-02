types_of_people = 10 #number of people variable
x = f"There are {types_of_people} types of people." #using variable in a string format that also has a variable with {} and f formatting

binary = "binary" #string as variable value
do_not = "don't" # another string is variable value and using single quote within double quote
y = f"Those who know {binary} and those who {do_not}." #using string and multiple variables within a string with with {} and f formatting

print(x) #printing x variable
print(y) #printing y variable

print(f"I said: {x}") #printing string with a variable with {} and f format
print(f"I also said: '{y}'") #printing string with a variable with {} and f format

hilarious = True #adding new variable after a number of commands above
joke_evaluation = "Isn't that joke so funny?! {}" #using {} to be able to use an active variable later on
z = "Damn Right it is funny!" #added this later to modify the original hilarious variable use with .format in the next line
print(joke_evaluation.format(z)) #showing the use of .format() within a print statement - combined 2 variables here
print(joke_evaluation.format(hilarious))

w = "This is the left side of..." #for displaying string placement+combination with (a+b format)
e = "a string with a right side." #for displaying string placement+combination with (a+b format)

print (w + e) # placing+combining two variables with addition operation
