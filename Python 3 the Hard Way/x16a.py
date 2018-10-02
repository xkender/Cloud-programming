from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "x")

print("Truncating the file. Goodbye!")
#target.truncate() # No need to use target.truncate() since we used "w" above which means truncating (cleaning) the file contents first.

print("Now I'm going to ask you for three lines.")

line1, line2, line3 = input("line 1: "), input("line 2: ")  , input("line 3: ")

print ("I'm going to write these to the file.")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))


print("And finally, we close it,")
target.close()


"""
Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	open for exclusive creation, failing if the file already exists
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newlines mode (deprecated)
The default mode is 'r' (open for reading text, synonym of 'rt'). For binary read-write access, the mode 'w+b'
opens and truncates the file to 0 bytes. 'r+b' opens the file without truncation.
"""
