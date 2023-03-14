# The Continue statment
'''
'Continue' is used to stop the current iteration of the loop and continue with the next one.
It instructs the program to "skip this iteration"

Ex:
    for i in range(4):
        print("printing")
        if i == 2:
            continue             ===>If i is 2, the iteration is skipped
        print(i)

'''

for i in range(10):
    if i == 5:
        continue
    print(i)