from sys import argv
from os.path import exists


script, from_file, to_file = argv # [scriptname, arg1, arg2]


#print(f'Copying from {from_file} to {to_file}')
print("Copying from {} to {}".format(from_file, to_file))

# We could do these two on one line, how?
# open(to_file, "w").write(open(from_file).read())

l = [1, "abc", 2.115, 3, -9]
print(len(l))


print(f'The input file is {len(indata)} bytes long')
howlong = len(indata)
print('The input file is {} bytes long'.format(howlong))


print(f'Does the output file exist? {exists(to_file)}')
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done,')

out_file.close()
in_file.close()
