from sys import argv

script, filename = argv

txt = open(filename) # txt = open(filename, encoding="utf-8")

print(f"Here is your file {filename}:")

print(txt.read())

print("Type the file name again:")
file_again = input("> ") # here we use input instead of argv to identify the file that needs to be opened...

txt_again = open(file_again)

print(txt_again.read())

txt_again.close


"""
#!/usr/bin/python3

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)

# Close opened file
fo.close()
"""
