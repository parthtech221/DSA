# Problem: Find even number
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def count_even(arr):
    count = 0
    for i in arr:
        if i%2==0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))   