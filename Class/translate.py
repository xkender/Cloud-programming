
eng_to_tur = {"one":"bir", "two":"iki", "three":"uc"}
engl = ["one", "two", "three"]
turl = ["bir", "iki", "uc"]

def translate_by_list(word, eng_to_tur = True):
    if eng_to_tur :
        idx = engl.index(word)
        print("Printing idx value: ", idx)
        return turl[idx]
    else:
        tdx = turl.index(word)
        print("Printing tdx value: ", tdx)
        return engl[tdx]

# second HW
#  1000 - 2000 arasinda 7 ve 11 e bolunebilen yada sadec 13 e bolunebilen sayilari bul

def translate(eng):
    return eng_to_tur[eng]

print(translate("one"))
print(translate_by_list("three"))
print(translate_by_list("uc", False))
