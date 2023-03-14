'''
 A spam comment is defined as a text containing following keywords:
"make a lot of money","buy now","subscribe this","click this". write a program to detect these spams.

'''


text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True

elif("buy now" in text):
    spam = True

elif("click this" in text):
    spam = True

elif("subscribe this" in text):
    spam = True

else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")


'''
if marks>=90:
    grade = "Ex"
elif markes>=80:
    grade = "A"
elif markes>=70:
    grade = "B"
elif markes>=60:
    grade = "c"
elif markes>=50:
    grade = "D"
else:
    grade = "F"

print("Your grade is" + grade)

'''