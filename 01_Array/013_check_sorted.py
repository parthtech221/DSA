# Problem: check sorted array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def sort_arr(arr):
    if len(arr) == 1:
        return "only one element"
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False

    return True

print(sort_arr([1, 2, 3, 6, 4, 5]))     