#Convert the tuple into a list to be able to change it:
x = ("apple","bnana","cherry")
y =list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


