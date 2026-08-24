# problem: Find Missing Number (Sum Formula)
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def missing_num(arr):
    n=arr[len(arr)-1]
    actual_sum=n*(n+1)//2
    sum=0
    for i in arr:
        sum+=i

    return actual_sum-sum

print(missing_num([1,2,3,5,6]))