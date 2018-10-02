"""
prints an x-mas tree
You can supply tree hight argument as integers, default is 10
"""

from sys import argv


"""
Default values to change, if you want to try other characters
"""
DEFAULT_ROWS = 10
DEFAULT_STAR = "#" # "#" #"\U0001F31F"  # "\u2605"
DEFAULT_LEAF = "*"
DEFAULT_TRUNK = "|"
DEFAULT_ORNAMENT = "."

STEM_LEN = 3
TRUNK_RATIO = 3
"""
"""

def print_top(rows):
    print((rows*2+5)*"_")

def print_bottom(rows):
    print((rows*2+5)*"-")

def print_text(rows):
    print("|", ((rows*2+5-20)//2)*" ", "MERRY CHRISTMAS!", ((rows*2+5-23)//2)*" ", "|", end="")

def print_empty_space(rows):
    print("|", ((rows*2+1)*" "), "|")

def print_space(length):
    print("|", length*" ",end="")

def print_spaceafter(length):
    print(length*" ", "|")

def print_star(rows, star=DEFAULT_STAR):
    print_space(rows)
    print(star, end="")
    print_spaceafter(rows)

def print_stand(rows, trunk=DEFAULT_TRUNK, stem=STEM_LEN):
    tsize = rows // TRUNK_RATIO
    if tsize % 2 == 0:
        tsize += 1
    for i in range(stem):
        print_space(rows - (tsize-1)//2)
        print(DEFAULT_TRUNK*tsize, end="")
        print_spaceafter(rows - (tsize-1)//2)

def is_ornamented(row):
    return row % 2 == 0

def print_ornament(row, ornament=DEFAULT_ORNAMENT):
    if is_ornamented(row):
        print(ornament, end="")

def print_space_for_leaves(rows):
    if is_ornamented(rows) : # need space for the ornament
        print_space(rows-1)
    else:
        print_space(rows)

def print_space_for_leaves_after(rows):
    if is_ornamented(rows) : # need space after the ornament
        print_spaceafter(rows-1)
    else:
        print_spaceafter(rows)

def get_number_of_leaves(rows, i):
    return  2*(rows+1-i)-1


def print_leaves(rows, i):
    print(get_number_of_leaves(rows, i)*DEFAULT_LEAF, end="")


def print_tree(rows):
    print_top(rows)
    print_star(rows)
    for i in range(rows, 0, -1):
        print_space_for_leaves(i)
        print_ornament(i)
        print_leaves(rows, i)
        print_ornament(i)
        print_space_for_leaves_after(i)
    print_stand(rows)
    print_empty_space(rows)
    print_text(rows)
    print()
    print_bottom(rows)

def main():
    try:
        script, size =  argv
        size = int(size)
    except:
        size = DEFAULT_ROWS
    print_tree(size)



if __name__ =="__main__":
    main()
