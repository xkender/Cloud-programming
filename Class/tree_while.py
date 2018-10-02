
def tree1(loop, repeat, char1, char2, char3, char4, char5, radius):
    current_number = 1
    while current_number <= loop:
        current_number += 1
        print(("  "*(radius-(radius-2))) + (f"{char3}"*(radius-8)))
        repeat += 1
        print(("  "*(radius-(radius-2))) + (f"{char2}"*(radius-8)))
        repeat += 1
        print(("  "*(radius-(radius-1))) + ("."*(radius-(radius-1))) + f"{char2}"*(radius-6) + ("."*(radius-(radius-1))))
        repeat += 1
        print(("  "*(radius-(radius-1))) + (f"{char2}"*(radius-4)))
        repeat += 1
        print(("."*(radius-(radius-1))) + f"{char2}"*(radius-2) + ("."*(radius-(radius-1))))
        repeat += 1
        print(f"{char2}"*radius)
        repeat -= 1
        print((" "*(radius-(radius-4))) + f"{char4}"*(radius-8))
        repeat -= 1
        print((" "*(radius-(radius-4))) + f"{char5}"*(radius-8))


tree1(1, 1, "#", "*", ".", "|", "_", 10)





#     #
#     *
#   .***.
#   *****
# .*******.
#    | |
#    ___



"""
def tree2(loop, repeat, char):
    current_number = 1
    while current_number <= loop:
        current_number += 1
        print(f"{char}"*repeat)

tree2(1, 1, "#")
tree2(1, 1, "*")
tree1(1, 4, "*")

"""




"""
def tree(char1, char2, char3, char4, char5, rows):
    for row in range(rows):
        whiletree(1, 1, char1)
        whiletree(1, 1, char2)

"""
