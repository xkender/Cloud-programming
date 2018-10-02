
filename = input("Please type in the file name you want to open: ")

txt = open(filename)

print(f"Here is your file to open: '{filename}', and below you can see its contents:")
print()
print(txt.read())

print("Type the file name again:")
file_again = input("> ")
print()
txt_again = open(file_again)

print(txt_again.read())
