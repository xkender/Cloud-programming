# 1000 - 2000 arasinda 7 ve 11 e bolunebilen yada sadece 13 e bolunebilen sayilari bul


def divisible_by(k, s, l, v, w):

    list1 = []
    list2 = []
    for i in range(v, w):
        if i % k == 0 and i % s == 0:
            list1.append(i)

        if i % l == 0:
            list2.append(i)

    print()
    print("Between {} and {}, there are".format(v, w), len(list1),"numbers divisible by {} and {}: ".format(k, s), list1, "\n")
    print("Between {} and {}, there are".format(v, w), len(list2), "numbers divisible by {}: ".format(l), list2, "\n")
    print(len(  set(list1) | set(list2) ))





def divisible_by_two_nums(i, firstnum, secondnum):
    return i % firstnum == 0 and i % secondnum == 0

def divisible_by_one_num(i, num):
    return i % num == 0

def how_many_divisible(firstnum, secondnum, num, start, end):
    count = 0
    for i in range(start, end):
        if divisible_by_one_num(i, num) or divisible_by_two_nums(i, firstnum, secondnum):
            count += 1
    return count

def main():
    count = how_many_divisible(7, 11, 13, 1000, 2000)
    print("there are ", count, " numbers divisible by 7 and 11 or 13 between 1000 - 2000 ")


if __name__ == "__main__":
    main()
    divisible_by(7, 11, 13, 1000, 2000)
