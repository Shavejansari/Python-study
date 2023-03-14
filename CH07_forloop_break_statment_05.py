#The Break statment
'Break is used to come out of the loop when encountered. It instruct the program to - Exit the loop now'
'''
EX:
    for i in range(0 ,80):
        print(i)
        if i == 3:
            break                 ---->This will print only 0,1,2,3 

'''


for i in range(10):
    print(i)
    if i == 5:
        break

else:
    print("This is inside else of for")
