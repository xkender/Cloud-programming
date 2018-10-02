i = 0
while i < 5:
  i += 1
  if i == 4:
      break
  print(i)

"""
i = 0
while i < 5:
  i += 1
  print(i)
"""
print("xxxxxxxxxxxxxxxxx")

for i in [1, 2, 3]:
    if i == 2:
        continue
    print(i)

print("xxxxxxxxxxxxxxxxx")

for i in [1, 2, 3]:
    if i == 2:
        pass
    else:
        print(i)
