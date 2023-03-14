#For Loop with else
'''
An optional else can be used with a for loop if the code is to be executed when the loop exhausts.
Ex:
    l = [1, 7, 8]
    for item in l:
        print(item)
    else:
        print("Done")     -->this is printed when the loop exhausts!

'''

for i in range(10):
    print(i)

else:
    print("Done")
    