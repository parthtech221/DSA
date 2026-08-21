# Problem: revrerse array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def revers(arr):
    n=len(arr)-1
    rev=[]
    for i in range(n,-1,-1):
        rev.append(arr[i])
    return rev
    

print(revers([1,2,3,5]))    
        