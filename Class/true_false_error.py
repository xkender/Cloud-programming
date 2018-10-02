


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
