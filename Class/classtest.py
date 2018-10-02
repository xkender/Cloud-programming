class Men():  #inheritance
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return str(self.age) + " "+ self.name

    def __gt__(self, rhs):
        return self.age > rhs.age


m1 = Men(3, "tim")

print(m1)
print(str(m1.age) + " "+ m1.name)

m2 = Men(4, "tommy")

if m1 > m2:
    print(" select m1 as a friend")
else:
    print(" select m2 as a friend")
