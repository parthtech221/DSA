# problem: Find Union Of Two Arrays
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def union(arr1,arr2):
    for i in arr1:
        count=False
        for j in arr2:
            if i==j:
                count=True
        if count==False:
            arr2.append(i)        
    return sorted(arr2)

print(union([1,2,3],[3,4,5]))            
