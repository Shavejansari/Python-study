# Write a python function to remove a given word from a string and strip it at the same time.


def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Harry is a good coder       "
n =remove_and_split(this, "Harry")
print(n)