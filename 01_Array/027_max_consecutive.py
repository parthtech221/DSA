# problem: maximun consecutive ones
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def consecutive_max(arr):
    count=0
    max_count = 0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
            if count>max_count:
                max_count=count
        else:
            count=0    
    return max_count

print(consecutive_max([1,1,1,1,1,0,1,1,1]))        