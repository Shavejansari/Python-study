#Write a program which finds out whether a given name is present in a list or not.

names = ["mohd", "shavej", "mukesh", "ashirwad","zapbuil"]
name = input(("Enter the name to check\n"))

if name in names:
    print("Your name is in the list")
else:
    print("Your name is not in the list")