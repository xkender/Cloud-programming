

def divisible_by_two_and_three(i):
    if i % 2 == 0 and i % 3 == 0:
        return True
    return False

assert(divisible_by_two_and_three(6))
assert(not divisible_by_two_and_three(7))
assert(not divisible_by_two_and_three(14))


def fancy_print(x):
    print("~ ", x," ~")

x = "tolga"
b = fancy_print(x)
# data types int flt bool
eng_to_tur = {"one":"bir", "two":"iki", "three":"uc"}
engl = ["one", "two", "three"]
turl = ["bir", "iki", "uc"]
print(b)
print(type(b))
print(type(3))
print(type(3.1))
print(type(x))
print(type(True))
print(type([]))
print(type(eng_to_tur))

def translate_by_list(word, eng_to_tur = True):
    if eng_to_tur :
        idx = engl.index(word)
        return turl[idx]
    else:
        # sen yaz
        pass


def translate(eng):
    return eng_to_tur[eng]

print(translate("one"))
print(translate_by_list("three"))
print(translate_by_list("uc", False))
