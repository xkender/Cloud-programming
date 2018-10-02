from sys import argv

script, input_file = argv

def print_all(f):
    #print(">>> Print_all: f=", f) #Adding print and to see the state of f at each point - "Debug prints"
    print(f.read())
    #print(">>> Print_all: f=", f)

def rewind(f):
    #print(">>> Rewind: f before seek(1)", f)
    f.seek(0) # Used f.seek(1) instead of f.seek(0) and it started reading the file from second letter...
    #print(">>> Rewind: f after seek(1)", f)
"""
QUESTION:
Why does seek(0) not set the current_line to 0?
First, the seek() function is dealing in bytes, not lines.
The code seek(0) moves the file to the 0 byte (first byte) in the file.
"""


def print_a_line(line_count, f):
    #print(">>> print_a_line: line count and f:", line_count, f )
    print(line_count, f.readline(), end="") #Added end="" to prevent addding extra space when this function is run.
    #print(">>> print_a_line: line count and f after readline:", line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
"""
Why are there empty lines between the lines in the file?
The readline() function returns the \n that’s in the file at the end of that
line. Add a end = "" at the end of your print function calls to avoid adding
double \n to every line.
"""

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1 # used "+= 1" instead of "current_line + 1" for a shorter version
print_a_line(current_line, current_file)
