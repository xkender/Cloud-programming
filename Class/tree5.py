"""
def c1(loop, repeat, char):
    current_number = 1
    while current_number <= loop:
        current_number += 1
        print((f"{char}"*repeat))
"""

def ch1(i):
    print(i)

def ch2(i):
    print(i, end=" ")

def ch3(k, l):
    print(f"{k}"*l)

def ch4(i, j):
    print(f"{i}"*j, end=" " )


def tree(a, b, c, d, e, f, g):
    current_number = 1
    while current_number <= g:
        current_number += 1
        ch3(c, f+5), ch3(d, f+1)
        ch4(a, f), ch4(a, f)


tree("#", ".", " ", "|", "*", 1, 10)



#print((f"{}"*(r-(r-1))) + (f"{}"*(r-(r-1))) + (f"{char2}"*(r-6) + (f"{}"*(r-(r-{}))))
