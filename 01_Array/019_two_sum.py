#problem: two sum brute force
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def two_sum(arr,target):
    n = len(arr)+1
    for i in range(n):
        for j in range(i,n):
            if (arr[i]+arr[j]) == target:
                return [i,j]
    return "not found"

print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))            