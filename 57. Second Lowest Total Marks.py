no_of_students = int(input("Enter no. of students: "))

names = []
grades = []

for j in range(1,no_of_students+1):
    name = input("Enter name of student: ")
    grade = int(input("Enter grade: "))
    names.append(name)
    grades.append(grade)

gradeList = list(zip(names,grades))

sorted_gradeList = sorted(gradeList, key = lambda x:x[1])
sorted_grades = sorted(set(grades))
second_lowest_score = sorted_grades[1]

anslist = []

for name,grade in sorted_gradeList:
    if grade == second_lowest_score:
        anslist.append(name)

print(anslist)
