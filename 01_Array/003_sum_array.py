# Problem: Find sum of element
# Difficulty:Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum    

print(sum([1, 2, 3, 4]))