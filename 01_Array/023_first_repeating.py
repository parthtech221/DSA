#problem: first repeating element
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def first_repeat(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return arr[i]
    return None

print(first_repeat([2, 5, 1, 2, 3, 5]))
print(first_repeat([1,2,3,4]))
print(first_repeat([7,7]))