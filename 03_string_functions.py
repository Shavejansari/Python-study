story = '''once upon a time there was a youtuber named Harry. 
who uploaded python cousres with notes Harry Harry Harry'''

# string Functions
print(len(story)) # returns 5.
print(story.endswith("notasd")) # This function tells whether the variable string ends with the string "rrr" or not if string is "Harry" it returns true for "rry" since Harry ends with rry.
print(story.endswith("notes")) #This function tells whether the variable string ends with the string "rrr" or not if string is "Harry" it returns true for "rry" since Harry ends with rry.
print(story.count("with")) #counts the total number of the accournce of any characters.
print(story.capitalize()) #This function capitilize the first charcters of a given strings. 
print(story.find("youtube")) #This function finds a word and returns the index of first occurence of that word in the string.
print(story.replace("Harry", "Shavej")) #This function replaces the odlword with the new word with newword in the entire string.
