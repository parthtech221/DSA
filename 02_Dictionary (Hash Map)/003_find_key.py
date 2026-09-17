# Problem: Find kay
# Difficulty:Easy
# Topic: hash map
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_key(students,name):
    return name in students

students = {
    "Alex": 20,
    "John": 25
}

print(find_key(students,'Alex'))