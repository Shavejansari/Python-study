def percent (marks):
    p = (int(marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

marks1 = [45, 89, 56, 54]
percentage1 = percent(marks1)


marks2 = [69, 76, 43, 59]
percentage2 = percent(marks2)
print(percentage1, percentage2)