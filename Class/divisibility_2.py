#import divisibility
#print(divisibility.how_many_divisible(2, 3, 5, 1, 100))

"""
from divisibility import how_many_divisible
from divisibility import divisible_by_one_num

print("2nd time ", how_many_divisible(2, 3, 5, 1, 100))

print(divisible_by_one_num(75, 5))
"""




def add(a, b):
  return a + b

def add2(a, b):
  total = a +b


total = add(2, 3)
print(total)

total2 = add2(2, 3)
print(total2)


"""
for range loop : all options
while loop
break / continue


bi sayinin faktoriyelini bolunebilen
5! = 5*4*3*2*1
0! = 1

what is the factorial of 1005 ?
"""

def pr(n):
  if n != 1 :
    pr(n-1)
  print(n, " ")

pr(10)
