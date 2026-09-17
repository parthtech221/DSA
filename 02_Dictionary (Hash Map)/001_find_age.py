# Problem: Find age
# Difficulty:Easy
# Topic: hash map
# Time Complexity: O(1)
# Space Complexity: O(1)

def find_age(students, name):
    return students[name]


students = {
    "Alex": 20,
    "John": 25,
    "Sara": 22
}

print(find_age(students, "John"))