import random as RND
fnx = lambda: [ RND.randint(10, 99) for c in range(10) ]
v1, v2, v3, v4 = fnx(), fnx(), fnx(), fnx()
