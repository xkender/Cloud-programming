from sys import argv

script, input_file, position = argv

def print_all(f):
    print(f.read())

def rewind(f, l):
    f.seek(l)

def print_a_line(line_count, f):
    print(line_count, f.readline())
    f.close

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file, 0)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

rewind(current_file, 1)
print(current_line)

print_a_line(current_line, current_file)
