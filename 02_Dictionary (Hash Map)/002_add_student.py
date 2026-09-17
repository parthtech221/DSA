# Problem: add element
# Difficulty:Easy
# Topic: hash map
# Time Complexity: O(1)
# Space Complexity: O(1)

def add_student(student,name,age):
    student[name]=age
    return student

student = {
    "Alex": 20
}

print(add_student(student, "Sara", 22))