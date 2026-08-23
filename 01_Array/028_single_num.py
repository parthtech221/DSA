# problem: Find single number in array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_single(arr):
    for i in range(len(arr)):
        count=0
        for j in range(i,len(arr)):
            if arr[i]==arr[j]:
                count+=1
            else:
                element=arr[i]         
        if count!=0:
            return element
        
    return None

print(find_single([4,1,2,1,4,3,5,5]))        