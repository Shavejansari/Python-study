#Write a python function to print first n line of the following pattern:

'''


* * * 
* * 
*               ====> for n=3


'''


n = 3
for i in range(n):
    print("*" * (n-i))