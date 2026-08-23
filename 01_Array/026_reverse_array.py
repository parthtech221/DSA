# problem: reverse array in place
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse(arr):
    n = len(arr)-1
    for i in range(len(arr)//2):
        arr[i],arr[n-i] = arr[n-i],arr[i]
    return arr    

print(reverse([1,2,3,4,5,6,7,8]))