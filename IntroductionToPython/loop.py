"""
"Definite" and "counted" loops:

for <var> in <sequence>:
    <body>

for i in range (10):  # i represents the "loop index"
     x = 3.9 * x * (1 - x)
     print (x)

"""

for i in [0, 1, 2, 3]: #counted loop
    print (i)

for odd in [1, 3, 5, 7, 9]: # counted loop
    print(odd * odd)

for i in range(10): # definite loop > "range" is a built in python function for generating a sequence of numbers "on the fly"

#asking pythong to turn "range" into a list to understand what it is:
# use this on python prompt >>> list(range(10)) #turns range(10) into an explicit list:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  Soru: Bunu nasil script icine koyabiliriz?
