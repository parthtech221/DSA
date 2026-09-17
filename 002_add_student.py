def add_student(student,name,age):
    student[name]=age
    return student

student = {
    "Alex": 20
}

print(add_student(student, "Sara", 22))