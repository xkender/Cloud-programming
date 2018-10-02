# Copyright Otuk 2018
#
# A tour of keywords and key features in python
#
# comments can go like  this - single line
#
"""
comments can also be in this multi-line
format.

"""

# import to use functions, objects, variables, definitions,
#  constants etc defined in a different python file / modules
import subprocess
import os

fn = "./test.txt" # a string variable named fn
fp = os.path.relpath(fn)  # construct a path object to file using imported definitions
# if and logical and, not, or for branching execution
# indentation for marking blocks/body of if/else
if not os.path.exists(fp) and not os.path.isdir(fp):
    # safer use of resources using "with - as" clause
    # after the with block oped file stream is closed automatically
    with open(fp, "w") as fos:
        fos.write("delete this")
        pass # with-as block ends here, pass is used to mean "do no operations"

    bash_args = ["cat", fn]
    subprocess.Popen(bash_args) # fork a process and execute command

    #import only what is needed with from - import
    from time import sleep

    ## just enough time to allow subprocess before remove removes
    sleep(1)
    os.remove(fp)
    print() # print a newline to stdout
    # program logic/execution check with asserts, if wrong program aborts with error string
    assert not os.path.exists(fp), "Unexpected"
else:
    # printing to stdout , multiple strings
    print("Either file ", fn, " exists, or cannot be opened for writing")


# lists - array like
li = [1, 2]  # define an array
# built-ins print, len and others
assert len(li) == 2, "Unexpected"  # get length with len()
li.append(3)
li.reverse() # method with side effect
assert li[0] == 3 # 0 based indexing
li.sort()
assert li[-1] == 3 # wraparound indexing, -1 means last

#li = [1,2,3]
x, y, *z = li  # itterable multi-assignment at once
assert y == 2, "Unexpected"
print(type(z), z)  # runtime type check, introspection, reflection
assert z == [3], "Unexpected"

#list comprehensions
li2 = [ n*n for n in li]
assert len(li2) == 3, "Unexpected"
assert li2[2] == 9, "Unexpected"
j = 0
for i in li2:
    assert li[j]*li[j] == i
    j += 1


# dictionary
D = {"test":1, "tost":2}
# remove the dictionary element from memory
del D["test"]
assert len(D) == 1 and D["tost"] == 2, "Unexpected"


#exception handling with try-catch-finally
try:
    assert D[0] == 2 # the D disctionary does not kave a key named 0
    assert False, "Unxpected"
except (KeyError):  # exceptions have names like ValueError
    assert(True)
finally:  # finally gets executed both when an execption occurs and when not
    D["new add"] = 3

assert len(D) == 2

# an example of a "not reccommeneded"
# dynamic reinterpretation using exec keyword
i=1
exec("assert i+1 == 2, 'Unexpected'")

x=3
# functions: def & return
def square(x):
    x += 1
    return x*x

y = square(x) # calling a function
assert x == 3, "Unexpected" # parameter passing by copy


lx=[3]
# function without return
# function parameter as a complex object and side effect
def square_and_append(lx):  # multi word function naming convention with _
    lx.append(lx[0])
    lx[0] = lx[0]*lx[0]

square_and_append(lx)
assert lx[0] == 9, "Unexpected"
assert len(lx) == 2 and lx[1] == 3, "Unexpected"

#function returns a function definition
def make_functions(y):
    def a_func(a, b):
        return a ** b + y  # exponent: a to the power b
    return a_func

f1 = make_functions(1)
f2 = make_functions(2)
assert 7 == make_functions(3)(4, 1), "Unecpected"
assert f1(2, 3) == 9, "Unexpected"
assert f2(2, 3) == 10, "Unexpected"


# using global:  to mean the global variable where
# it might be hidden by a lower scope variable definition
x = 3
y = 2
def add (a, y):
    global x
    return x + a + y

assert 11 is add(4,4), "Unexpected"


# class : a user defined type, OOP in python
# __init__, __str__ magic functions
# self
class Person:
    def __init__(self, name, age):
        self.name = name  #instance variable
        self.age = age

    def getAge(self):  # instance method
        return self.age

    def __str__(self):
        return self.name

# inheritance
class Employee(Person):
    def __init__(self, name, age, title):
        Person.__init__(self, name, age)
        self.title = title

    #overwriting a method
    def __str__(self):
        return self.title + " "+ self.name

# instantiation of objects
p1 = Person("Smith", 23) # calls __init__ method
p2 = Person("Jones", 41)
# automatic conversion to string reprsentation via __str__
print(p1)
print(p2)
e1 = Employee("Wall", 32, "Mrs.")
e2 = Employee("Odell", 55, "President")
print(e1)
print(e2)

print(e2, " is ", e2.getAge(), " years old") # inheritted method
# string concatanation
# and int to string conversion.  similarly int("str") converts to int.
print(p1, " is " + str(p1.getAge()) + " years old")


# @decorators
# and composition
class Car (object):  # all objects inherit from object by default
    count = 0  # a class level variable

    @classmethod  # makes this method a class method
    def howMany(cls):  # cls instead of self as we refer to the class itself not an instance
        return cls.count

    def __init__(self, doors=4, person=None):  # duck typing, what is person?
        self.doors = doors
        self.owner = person  # class composed of other classes
        Car.count += 1  # using a class level variable


c1 = Car(4)
c2 = Car(2, e1)
assert Car.howMany() == 2
assert c2.howMany() == 2
assert c1.doors == 4
assert c1.count == 2
assert c1.howMany() == 2

print("Car c2 is owned by ", c2.owner) # automatic conversion to string by use of  __str__

#function returning class
def CycleFactory(DEF_COLOR, wheels=2):
    class Unicycle:
        wheels = 1
        def __init__(self, color = DEF_COLOR):
            self._color = color
        def color(self):
            return self._color
    class Bike(Unicycle):
        wheels = 2
        def __init__(self, color = DEF_COLOR):
            self._color = color
    class Trike(Unicycle):
        wheels = 3
        def __init__(self, color = DEF_COLOR):
            self._color = color
    if wheels == 2:
        return Bike
    elif wheels == 1:
        return Unicycle
    else:
        return Trike

Cycle = CycleFactory("red")
c1 = Cycle("blue")
TCycle = CycleFactory("red", wheels=3) # passing arguments by name
c2 = TCycle()
assert c1.wheels == 2 and c1.color() == "blue", "Unexpected"
assert c2.wheels == 3 and c2.color() == "red", "Unexpected"


# a more abstract use of a class
# helps with separating problems into smaller sections
class HowManyTimes:
    def __init__(self, i):
        self._i = i

    def next(self):
        if self._i is 0:
            return False
        else:
            self._i -= 1
            return True


once = HowManyTimes(1)

# for loops and simple range based looping
for i in range(10, -1, -1):
    if once.next() :
        assert i == 10, "Unexpected"
    else:
        assert i != 10, "Unexpected"


twice = HowManyTimes(2)
i = 0
while twice.next(): # while loop
    i += 1
assert i == 2, "Unexpected"


# lambda functions and closures
y = 0
def make_adder(i):
    return lambda x : x + i + y

five_adder = make_adder(5)
assert five_adder(3) == 8, "Unexpected"

nine_adder = make_adder(9)
assert nine_adder(3) == 12, "Unexpected"

y = 1  # the lamdabehavior can be changed by changing the enclosed y
assert five_adder(3) != 8, "Unexpected"


# generators, yield
# break, continue
def counter(max):
    i = 0
    while True:
        yield i
        i += 1
        if i >= max:
            break

countUntil = counter(3)
looping = False
for i in countUntil:
    looping = True
    assert i < 3, "Unexpected"
assert looping, "Unexpected"

nums = counter(100)
print(sum(nums)) # an example use for generators

nums = counter(10000000)
# here a list of 10M elements is not created in memory, but each number
# is generated one by one when needed, hence one of the uses of generators
print(sum(nums))


### end of a single session python language by example ####
