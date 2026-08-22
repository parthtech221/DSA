#problem: remove duplicat
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def remove_dup(arr):
    new_arr = []
    for i in range(0,len(arr)):
        if arr[i-1]!=arr[i]:
            new_arr.append(arr[i])
    return new_arr        
    
print(remove_dup([1,1,2,2,3,4,4,5]))        