def c1(loop, repeat, char):
    current_number = 1
    while current_number <= loop:
        current_number += 1
        print((f"{char}"*repeat))

def c2(loop, repeat, char):
    current_number = 1
    while current_number <= loop:
        current_number += 1
        print((f"{char}"*repeat), end=" ")

def tree():
    c1(1, 1, "   #")
    c1(1, 1, ".*****.")
    c1(1, 1, "********")
    c1(1, 1, "********")

tree()
