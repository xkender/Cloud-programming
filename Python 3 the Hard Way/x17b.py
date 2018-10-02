from sys import argv

script, from_file, to_file = argv

# We could do these two on one line, how?
in_file = open(from_file)
print(in_file.read())
indata = in_file.read()


out_file = open(to_file, 'r+')
out_file.write(indata)
print(out_file.read())

out_file.close()
in_file.close()
