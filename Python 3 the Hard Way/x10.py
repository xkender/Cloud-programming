tabby_cat = "\tI'm tabbed in." #using backslash as an escape sequence for horizontal tab
persian_cat = "I'm split\non a line." #using backslash as an escape sequence for new lines
backslash_cat = "I'm \\ a \\ cat."

# We can't use # between """ """
fat_cat = """
# below is using backslash as an escape sequence for \t horizontal tab
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
