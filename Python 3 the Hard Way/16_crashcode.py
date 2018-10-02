from sys import argv
from os.path import exists # importing exist command to check if a file exists

script, filename = argv

print(f'Does the output file exist? {exists(filename)}') #using exists we first check if the file is present - returns TRUE or FALSE

target = open(filename, "w")

target.truncate

line1 = "Free__"

i = 0
while i < 10:
    i += 1
    target.write("{}".format(line1))

target = open(filename)

print(target.read())

target.close()

#QUESTION: Do we have to use read mode after write mode to be able to read
#out the file contents.
