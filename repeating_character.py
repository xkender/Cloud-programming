
def firstRepeatedChar(str):

    h = {}  # Create empty hash

    # Traverse each characters in string
    # in lower case order
    for ch in str:

        # If character is already present
        # in hash, return char
        if ch in h:
            return ch;

        # Add ch to hash
        else:
            h[ch] = 0

    return '\0'


print(firstRepeatedChar("freedom"))


"""
def repeating_character(word):

    list = {}

    for character in word:
        if character in h:
            return character;
        else:
            list[character] = 0

repeating_character(freedom)
"""
