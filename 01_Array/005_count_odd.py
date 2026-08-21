# Problem: Find odd number
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def count_odd(arr):
    count = 0
    for i in arr:
        if i%2!=0:
            count += 1
    return count

print(count_odd([1, 2, 3, 4, 5]))   