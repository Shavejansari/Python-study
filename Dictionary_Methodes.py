myDict = {
    "mohd" : "Is DevOps Engineer intern.",
    "harry" : "A coder",
    "marks" : [1, 2, 3, 5],
    "anotherdict": {'harry':'player'},
    1: 2,
    "devops": "Engineer"
}
print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values())#prints the values of the dictionary
print(type(myDict.keys()))#prints the type of the dictionary
print (myDict.item()) #prints the (keys, value) for all contents of the dictionary