from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")


line1, line2, line3 = input("line 1: "), input("line 2: "), input("line 3: ")
#used above code instead of below to make it shorter
"""
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
"""

print ("I'm going to write these to the file.")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))
#used above code instead of below to make it shorter
"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""

print("Opening the file...")
target = open(filename)

print("Here is your file with the new contents:")
print(target.read())

print("And finally, we close it,")
target.close()

#Don't forget to close all your files since memory leak might occur and crash
#the computer for bigger files.
#Python automatically saves the file if you forget to close it...
