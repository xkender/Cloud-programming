#simple notes

def loop_it():
    print("starting run")
    for i in range(2**20):
        pass
    print("ending run")


def f_to_c(fahr_val):
    return (fahr_val - 32) / 2

def c_to_f(cel_val):
    return (cel_val * 2) + 32


import subprocess


if __name__ == "__main__":
    # decimalvar = "101"
    # binaryvar = "101"
    # hexvar = "10G"
    # print(int(decimalvar, 10))
    # print(int(binaryvar, 2))
    # print(int(hexvar, 17), 17*17+16)

    # PEMDAS
    # cel = 0
    # fval = c_to_f(cel)
    # cval = f_to_c(fval)
    # print(cel, fval, cval)
    # print(c_to_f(f_to_c(c_to_f(100))))
    # completed = subprocess.run(['ls', '-l'])
    # print(completed)0
    # print(completed.returncode)
    # print(completed.args)

    # y = 3
    # y += 1 # y = y+1
    # print(y)
    # name = "isko"
    # prompt = "{} enter a number, but not {} "
    # prompt = prompt.format(name, y).capitalize() #  "isko enter a number, but not 4 "
    #
    # i = input(prompt)
    # print(i)

    #  c version
    #
    # for(int i = 0; i<10; i++){
    #     printf("%d", i);
    # }

    for i in range(10):
        print()
        for j in range(10):
            print("{}-{}".format(i, j), end=" ")

    print()
    print("ended loop")
