def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def get_coordinates():
    pass
    return 30.1, 54.3

x, y = get_coordinates()

def fetch_data_from_DB(userid, passwd):
    """
    establish
    sql connection
    get sql data
    """
    data = ["iskender", "orhan"]
    error = False # adding error variable (and setting it as "False") in case unable to get expected return from database connection
    return error, data # returning both data and error in case unable to get expected return from database connection
                       #

error, data = fetch_data_from_DB("tolga", "pass")
if not error:
    # do something with data
    pass

def divide(a, b):
    if b == 0 :
        error = True
        result = None
    else :
        result = a/b
        error = False    # adding error in case unable to get expected return
    return error, result # python lets returning more than one value

my_share = 1
error, result = divide(12, 2)
if not error :
    my_share += result
print(my_share)

error, result = divide(12, 0)
if not error :
    my_share += result
print(my_share)


for i in range(10, 0, -2):
    if i == 4:
        break     # goes to the end of the function
    if i == 10:
        continue  # skips the condition and moves to next loop item
    print(i)
    print(i)
    pass

# print a xmas tree height 10 rows with star at top
# and hanging decorations every other row
#


                            #     #
                            #     *
                            #   .***.
                            #   *****
                            # .*******.
                            #    | |
                            #    ___
