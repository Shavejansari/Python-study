# Write a program to fill in a letter template given below with name and date.

Name = input("Enter your name\n")
Date = input("Enter Date\n")



letter = '''Dear <|Name|>,
You are selected!
Date: <|Date|>
'''
letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)
print(letter)
