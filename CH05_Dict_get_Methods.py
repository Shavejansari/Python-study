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
print(myDict.get("Shavej")) #Print the value associated with key
print(myDict["Shavej"]) ##Print the value associated with key


#The difference between .get and [] syntax in dict?
print(myDict.get("Shavej2")) #Returns none as Shavej2 is not present in the dict
print(myDict["Shavej2"]) #Throws an error as Shavej2 is not present in the dict