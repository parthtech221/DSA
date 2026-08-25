# problem: find intersection of two array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n*m)
# Space Complexity: O(k)

def intersection(arr1,arr2):
    new_arr=[]
    for i in arr1:
       for j in arr2:
           if i==j:
                new_arr.append(j)
    return new_arr

print(intersection([1,2,3,4],[3,4,5,6]))        
print(intersection([2,4,5],[5,1]))
