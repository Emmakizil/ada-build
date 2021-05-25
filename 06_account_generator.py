import random

student_name = []
for i in range(5):
    name = input("Enter student's first and last name? ")
    student_name.append(name)

student_ID = []
for student in student_name:
    SID = random.randint(111111, 999999)
    student_ID.append(SID)

student_email = []
i=0
for name in student_name:
    [first, last] = name.split(" ")
    student_email.append(first[0]+last+str(student_ID[i])[-3:]+"@example.org")

for i in range(5):
    print(f"name: {student_name[i]}")
    print(f"id: {student_ID[i]}")
    print(f"email: {student_email[i]}")