# problem: remove duplicate in O(1) space
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)
 
def remove_dupli(arr):
    previous = 0
    for i in arr[1:]:
        if arr[previous]==i:
            arr.remove(i)
        if arr[previous]!=i:
            previous+=1
            
    return arr 

print(remove_dupli([1,1,2,2,3,4,4]))
print(remove_dupli([1,1,1,1]))