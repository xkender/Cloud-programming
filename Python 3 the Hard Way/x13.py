
from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv
four = input("What is between 3rd and 5th?: ")


print("The script is called:", script)
print("The first is called:", first)
print("The second is called:", second)
print("The third is called:", third)
print("The fourth is called:", four)

"""
This script should be run with below command:
python x13.py first 2nd 3rd

If you run:
python x13.py
You get below error:
Traceback (most recent call last):
  File "x13.py", line 4, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 1)

if you run:

python3.6 x13.py stuff things that
You get below:
The script is called: x13.py
The first is called: stuff
The second is called: things
The third is called: that

QUESTION: When why do we use the variables in the code?

"""
