

threes = []
for x in range(1,10):
    threes.append(x**3)
print(threes, end=' ')

# Returns sum of all digits in numbers
# from 1 to n
def sumOfDigitsFrom1ToN(n) :

    result = 0   # initialize result

    # One by one compute sum of digits
    # in every number from 1 to n
    for x in range(1, n+1) :
        result = result + sumOfDigits(x)

    return result


"""
squares2 = []
for y in range (10):
    squares2.append(y**3)
print(squares2, end=" ")

squares3 = []
for z in range (10):
    squares3.append(z**3)
print(squares3, end=" ")

arm = squares + squares2 + squares3
print(arm)
"""


"""
print(armstrong)
if armstrong == (squares + squares2 + squares3):
    print(armstrong)
else:
    print("nothing here")
"""
