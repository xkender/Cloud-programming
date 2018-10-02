"""
prints an x-mas tree
You can supply tree hight argument as integers, default is 10
"""

from sys import argv
from sys import stdout

"""
Default values to change, if you want to try other characters
"""
DEFAULT_OUTFILE = stdout

DEFAULT_ROWS = 10
DEFAULT_STAR = "#" # "#" #"\U0001F31F"  # "\u2605"
DEFAULT_LEAF = "*"
DEFAULT_TRUNK = "|"
DEFAULT_ORNAMENT = "."


STEM_LEN = 3
TRUNK_RATIO = 3
"""
"""

def card_print(word, dest=stdout):
    dest.write(word)

def print_space(length, dest=stdout):
    card_print(length*" ", dest)

def print_borders(rows, i, dest=stdout):
    if i == 0 or i == -1:
        card_print((2*(rows+2)- 1)*"=", dest)
        card_print("\n", dest)
    else:
        card_print("|", dest)

def print_star(rows, star=DEFAULT_STAR, dest=stdout ):
    print_borders(rows, rows, dest)
    print_space(rows, dest)
    card_print(star, dest)
    print_space(rows, dest)
    print_borders(rows, rows, dest)
    card_print("\n", dest)


def print_stand(rows, trunk=DEFAULT_TRUNK, stem=STEM_LEN, dest=stdout):
    tsize = rows // TRUNK_RATIO
    if tsize % 2 == 0:
        tsize += 1
    for i in range(stem):
        print_borders(rows, rows, dest)
        print_space(rows - (tsize-1)//2, dest)
        card_print(DEFAULT_TRUNK*tsize, dest)
        print_space(rows - (tsize-1)//2, dest)
        print_borders(rows, rows, dest)
        card_print("\n", dest)

def is_ornamented(row):
    return row % 2 == 0

def print_ornament(row, ornament=DEFAULT_ORNAMENT, dest=stdout):
    if is_ornamented(row):
        card_print(str(ornament), dest)

def print_space_for_leaves(rows, dest=stdout):
    if is_ornamented(rows) : # need space for the ornament
        print_space(rows-1, dest)
    else:
        print_space(rows, dest)

def get_number_of_leaves(rows, i):
    return  2*(rows+1-i)-1

def print_leaves(rows, i, dest=stdout):
    card_print(get_number_of_leaves(rows, i)*DEFAULT_LEAF, dest)




def print_tree(rows, dest):
    print_borders(rows, -1, dest)
    print_star(rows, dest=dest)
    for i in range(rows, 0, -1):
        print_borders(rows, i, dest)
        print_space_for_leaves(i, dest=dest)
        print_ornament(i, dest=dest)
        print_leaves(rows, i, dest=dest)
        print_ornament(i, dest=dest)
        print_space_for_leaves(i, dest=dest)
        print_borders(rows, i, dest)
        card_print("\n", dest=dest)
    print_stand(rows, dest=dest)
    print_borders(rows, 0, dest)


def main():
    try:
        script, *pair  =  argv
        if  len(pair) ==2:
            size = int(pair[0])
            dest = open(pair[1], "w")
        elif len(pair) == 1:
            size = int(pair[0])
            dest = DEFAULT_OUTFILE
        else:
            size = DEFAULT_ROWS
            dest = DEFAULT_OUTFILE
    except :
        size = DEFAULT_ROWS
        dest = DEFAULT_OUTFILE
    print_tree(size, dest)
    dest.close()



if __name__ =="__main__":
    main()
