def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b#, a % b, a / b

age = add(30, 11)
weight = sub(200, 20)
height = multiply(10, 8)
iq = divide(300, 2)

print(f"Age: {age}, Weight: {weight}, Height: {height}, iq: {iq}")

what = add(age, sub(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

"""
Why does Python print the formula or the functions “backward”? It’s not really
backward, it’s “inside out.” When you start breaking down the function into
separate formulas and function calls you’ll see how it works. Try to understand
what I mean by “inside out” rather than “backward.”

"""

#PEMDAS = Paranthesis, Exponents, Multiplication, Division, Addition, Subtraction
"""That’s the order Python follows as well. The mistake people make with PEMDAS is
to think this is a strict order, as in “Do P, then E, then M, then D, then A,
then S.” The actual order is you do the multiplication and division (M&D) in one
step, from left to right, then you do the addition and subtraction in one step
from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S)."""

"""
How can I use input() to enter my own values? Remember int(input())?
The problem with that is then you can’t enter floating point,
so also try using float(input()) instead.
"""
