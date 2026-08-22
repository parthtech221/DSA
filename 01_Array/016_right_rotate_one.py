#problem: right rotate 
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def rotate_right(arr,target):
    left = []
    for i in arr[target:]:
        left.append(i)
    for i in arr[:target]:
        left.append(i)
    return left

print(rotate_right([1, 2, 3, 4, 5],2))        
        