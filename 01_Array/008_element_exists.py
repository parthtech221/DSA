# Problem: element in array 
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def elementexists(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return "true"
    if arr[i]!=target:
        return 'false'    
        
print(elementexists([5,8,1,9],8))        
        
    