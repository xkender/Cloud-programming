def draw(char, count):
    for counts in range(count):
        print(f"{char}")

def draw2(char, count):
    for counts in range(count):
        print(f"{char}", end=" " )

def tree(char1, char2, char3, char4, char5, rows):
    for row in range(rows):
        if row == 0:
            draw(f"    {char1}", 1)
        if row == 1:
            draw(f"    {char2}", 1)
        if row == 2:
            draw2(f"{char3}", 1)
            draw2(f"{char2}", 3)
            draw(f"{char3}", 1)
        if row == 3:
            draw2(f"{char2}", 5)
            print()
        if row == 4:
            draw2(f"{char3}", 1)
            draw2(f"{char2}", 7)
            draw(f"{char3}", 1)
        if row == 5:
            draw(f"{char4}", 2)
        if row == 6:
            draw(f"{char5}", 2)

tree("#", "*", ".", "/", "_", 7)
