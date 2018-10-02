
def charac_count(word, target_repeated=2):
    # empty dictionary
    dict_c = {}
    # print(dict_c) #seeing inside the empty dictionary

    for char in word: #assigning 0 value for each character in the word
        dict_c[char] = 0
    # print(dict_c) #seeing inside the modified dictionary

    how_many_repeated = 0
    for char in word: # assigning original value plus one to each character
       dict_c[char] += 1
       if dict_c[char] == 2:
           if how_many_repeated == target_repeated:
               return char
           how_many_repeated += 1
           #return char
    return None
    # print(dict_c) #since each character is unique value increases when repeats



k = charac_count("aabcb")
print("First repeating character is:", k, "and count is:", 2)
print("First repeating character is:", charac_count("abc"), "and count is:", 2)
print("First repeating character is:", charac_count("acbcb"), "and count is:", 2)
print("First repeating character is:", charac_count("zacbzcb"), "and count is:", 2)
print("First repeating character is:", charac_count("eeaacbcb"), "and count is:", 2)
print("First repeating character is:", charac_count("abcdfghijklmnzzeeacbcb"), "and count is:", 2)


#li = [c for c in "acbcb"]
li = []
s = set()
word = "abcdfghijklmnzzeeacbcb" #"abcbc"
for c in word:
    li.append(c)
    s.add(c)
    if len(s) != len(li):
        print(c)
        break
