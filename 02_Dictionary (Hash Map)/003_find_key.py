def find_key(students,name):
    return name in students

students = {
    "Alex": 20,
    "John": 25
}

print(find_key(students,'Alex'))