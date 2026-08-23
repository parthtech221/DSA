# problem: check palindrome array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse(arr):
    n = len(arr)-1
    for i in range(len(arr)//2):
        if arr[i]==arr[n-i]:
            return True
    return False    

print(reverse([1,2,3,2,1]))