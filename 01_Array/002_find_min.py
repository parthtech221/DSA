# Problem: Find Minimum Element
# Difficulty:Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_min(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min

print(find_min([3,7,2,9,1]))        