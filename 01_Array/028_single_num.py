# problem: Find single number in array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_single(arr):
    for i in arr:
        count=0
        for j in arr:
            if i==j:
                count+=1
        if count==1:
            return i        
      
    return None

print(find_single([4,1,2,1,4,3,5,5,2,3,6]))        