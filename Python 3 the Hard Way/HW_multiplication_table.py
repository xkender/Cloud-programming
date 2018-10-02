
"""
solutions for multiplication table
"""

"""
soln. 1
"""
# for i in [1, 6]: #range(1,3) => [1, 2, 3]
#     print("\n")
#     for j in range(1, 11): #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         i1, i2, i3, i4, i5 = i, i+1, i+2, i+3, i+4
#         print("{:2} x {:2} = {:3}   {:2} x {:2} = {:3}   {:2} x {:2} = {:3}   {:2} x {:2} = {:3}   {:2} x {:2} = {:3}".format(
#         i1, j, i1*j, i2, j, i2*j, i3, j, i3*j, i4, j, i4*j, i5, j, i5*j ))

"""
soln. 2
"""
for i in [1, 6]:
    print("\n")
    for j in range(1, 11):
        for k in range(5):
            print("{:2} x {:2} = {:3}".format(i+k, j, (i+k)*j), end= "   ")
        print()
