#Range of Indexes
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #This example returns the items from the beginning to, but NOT included, "kiwi":



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #This example returns the items from "cherry" and to the end:



#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #This example returns the items from index -4 (included) to index -1 (excluded)

