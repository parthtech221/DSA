# problem: Find single number ina array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_single(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]!=arr[j]:
                return arr[i]
    return None

print(find_single([4,1,2,1,2]))        