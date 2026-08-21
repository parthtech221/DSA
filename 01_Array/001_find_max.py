# Problem: Find Maximum Element
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_max(arr):
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    return max

print(find_max([3, 7, 2, 9, 1]))
