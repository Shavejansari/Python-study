myDict = {
    "mohd" : "Is DevOps Engineer intern.",
    "harry" : "A coder",
    "marks" : [1, 2, 3, 5],
    "anotherdict": {'harry':'player'},
    1: 2,
    "devops": "Engineer"
}


print(myDict)
updateDict = {

    "Shubham" : "Friend",
    "Sonu" : "Friend",
    "Shavej":  "Engineer",

}
myDict.update(updateDict) #update the dictionary by adding key-value pairs from updateDict
print(myDict)
print(myDict.get("Shavej"))