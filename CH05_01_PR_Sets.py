#Write a program to create a dictionary of Hindi words with values as their english translation.Provide user with an option to look it up!




myDict = {
    "Kursi": "Chair",
    "Kitaab": "Book",
    "Ghari": "watch"
}
print("options are ", myDict.keys())
a= input("Enter the Hindi Word\n")
#below line will not throw an error if the key is not present in the dict
print("The meaning of your word is:", myDict.get(a))
