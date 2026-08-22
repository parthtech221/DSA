#problem: left rotate 
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def rotate_left(arr,target):
    left = []
    n = len(arr) - target
    for i in arr[n:]:
        left.append(i)
    for i in arr[:n]:
        left.append(i)
    return left

print(rotate_left([1, 2, 3, 4, 5],2))        
        