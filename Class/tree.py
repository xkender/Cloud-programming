# print a xmas tree height 10 rows with star at top
# and hanging decorations every other row
#
"""
az kod yaz loop kullan
pattern var
1 le basliyosun 10 tane row olcak
every other row put a decoration
tepede christasmas sus
altta base
functions, loop, if else kullan
decoration bazen var bazen yok
"""
                            #     #
                            #     *
                            #   .***.
                            #   *****
                            # .*******.
                            #    | |
                            #    ___
"""
def stars(star, dot, slash, underscore)
    if character = star :
        character = int(character)
        for star in range(character):
            print
"""





def tree(char1, char2, char3, char4, char5, rows):
    for row in range(rows):
        if row == 0:
            print(f"      {char1}")
        if row == 1:
            print(f"      {char2}")
        if row == 2:
            print(f"    {char3}{char2}{char2}{char2}{char3}")
        if row == 3:
            print(f"    {char2}{char2}{char2}{char2}{char2}")
        if row == 4:
            print(f"  {char3}{char2}{char2}{char2}{char2}{char2}{char2}{char2}{char3}")
        if row == 5:
            print(f"     {char4} {char4}")
        if row == 6:
            print(f"     {char5}{char5}{char5}")


tree("#", "*", ".", "/", "_", 8)
