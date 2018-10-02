from sys import argv

script, filename = argv

txt = open(filename)

print(f"Name of your file is: {filename}", "Please confirm if 'yes' or 'no':")
a = input()

if a == "no":
    print("Closing your file, since you don't want to open it...")
else:
    print("Below you can find your file contents:")
    print(txt.read())

txt.close

#for a in ["yes", "no"]:
