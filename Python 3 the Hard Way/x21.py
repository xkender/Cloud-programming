
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def sub(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def mult(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def div(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's just do some math with functions!! :) ")

age = add(30, 5)
print(">>> ", age) #debug printing to see the value of age.
height = sub(78, 4)
weight = mult(90, 2)
iq = div(100, 2)

print(f"Age: {age}, Height: {height}, weight: {weight}, iq: {iq}")

# A Puzzle for extra credit, type it anyway.

print()
print("Here is a puzzle")

what = add(age, sub(height, mult(weight, div(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print()
print()
