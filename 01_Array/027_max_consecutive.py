# problem: maximun consecutive ones
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def consecutive_max(arr):
    count=0
    for i in range(1,len(arr)):
        if arr[i-1]==arr[i]:
            count+=1
    return count

print(consecutive_max([1,1,0,1,1,1]))        