#Write a program to greet all the person names stored in a list l1 and which starts with 5.
#                   l1=["Harry","Subham","sachin","Rahul"]

l1=["Harry","Subham","Sachin","Rahul","Sohan"]

for name in l1:
    if name.startswith("S"):
        print("Hello\t" + name)
    # elif name.startswith("S"):
    #     print("You are not authorized person\t" + name)