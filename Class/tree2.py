def tree(star, dot, pound, slash, underscore, rows):
    for row in range(rows):
        if row == 0:
            print(f"      {pound}")
        if row == 1:
            print(f"      {star}")
        if row == 2:
            print(f"    {dot}{star}{star}{star}{dot}")
        if row == 3:
            print(f"    {star}{star}{star}{star}{star}")
        if row == 4:
            print(f"  {dot}{star}{star}{star}{star}{star}{star}{star}{dot}")
        if row == 5:
            print(f"     {slash} {slash}")
        if row == 6:
            print(f"     {underscore}{underscore}{underscore}")


tree("0", "1", "9", "o", "6", 200)
