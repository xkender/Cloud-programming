from sys import argv
from os.path import exists


script, from_file, to_file = argv # [scriptname, arg1, arg2]


#print(f'Copying from {from_file} to {to_file}')
#print("Copying from {} to {}".format(from_file, to_file))

# We could do these two on one line, how?
#in_file, indata = open(from_file), in_file.read()

in_file = open(from_file)
indata = in_file.read()

print(f'The input file exists?{exists(to_file)}, and is {len(indata)} bytes long')

#print(f'Does the output file exist? {exists(to_file)}')

#removing below user input...
#print('Ready, hit RETURN to continue, CTRL-C to abort.')
#input()

out_file = open(to_file, 'w')
out_file.write(indata)
out_file = open(to_file)

#print(f"Copy and paste to {out_file}")

out_file.close()
in_file.close()
