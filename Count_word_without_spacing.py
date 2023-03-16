
str = "myNameIsMdIqbal"

def count_words_without_spacing(s):
    word_count = 1  
    for i in range(len(s)):
        if s[i].isupper():
            word_count += 1
    print(f"{word_count}")



count_words_without_spacing(str)  # output: 5 words
