#Write a program to print multiplication table of n using for loop in reversed order


num = int(input("Enter the number "))
limit = int(input("Enter the ending : "))
for i in range(limit, 0,-1):
#     #print(str(num) + " X " + str(i) + "=" + str(i*num)

    print(f"{num}X{i}={num*i}"[::-1])
# #     txt = (f"{num}X{i}={num*i}[::-1]")

# txt = "Hello World"[::-1]
# print(txt)

