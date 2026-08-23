#problem: majority element 
# Difficulty: easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def majority(arr):
    for i in arr:
        count=0
        for j in arr:
            if j==i:
                count+=1
        if count>len(arr)//2:
            return i
    return "no majority element"             
    

print(majority([1, 2, 2, 2, 3]))