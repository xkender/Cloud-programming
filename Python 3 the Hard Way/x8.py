formatter = "{} {} {} {} {}" #Adding variable  with {} in order to use format function below

print(formatter.format(1, 2, 3, 4, 5)) # Using numbers for .format function
print(formatter.format("one", "two", "three", "four", 5)) # using string with format function
print(formatter.format(True, False, False, True, False)) # using boolean with format function
print(formatter.format(formatter, formatter, formatter, formatter, formatter)) #using variable with format function
print(formatter.format( #displaying the usage of multiple line typing for line displaying of a string (sentence)
# Mistake: While typing, I forgot to add commas after each string below which gave IndexError
    "What does the Billboard say?", #adding comma to each line of string
    "Come and play! Come and play!", #adding comma to each line of string
    "Forget about the moment!", #adding comma toeach line of string
    "Do not!", #adding comma to each line of string
    "Wake up!" # no comma added since this is the last line of the whole string. Also since this the 5th line where formatter has 4 {}. It will not be displayed in command prompt.
    )) #how to end the multiple row string
