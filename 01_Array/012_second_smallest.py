# Problem: find second smallest element
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def second_smallest(arr):
    if len(arr) < 2:
        return None

    smallest = arr[0]
    second_smallest = None

    for num in arr[1:]:

        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num != smallest and (
            second_smallest is None or num < second_smallest
        ):
            second_smallest = num

    return second_smallest 

print(second_smallest([5, 2, 8, 1, 9]))