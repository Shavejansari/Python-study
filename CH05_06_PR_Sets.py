#problem 5
#create an empty dictionry. Allow 4 frinds to enter their favourite language as values and use keys as their names. Assume that the names are uniqe.





#If names of 2 friends are same; What will happen to the program in problem 6?
Favlang = {}
a = input("Enter your Faverite language Shubham\n")
b = input("Enter your Faverite language Bilal\n")
c = input("Enter your Faverite language Aamir\n")
d = input("Enter your Faverite language Ankit\n")

Favlang['Shubham'] = a
Favlang['Bilal'] = b
Favlang['Aamir'] = c
Favlang['Shubham'] = d

print(Favlang)