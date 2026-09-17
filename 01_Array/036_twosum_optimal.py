# problem: Find two sum in array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def twosum(array,target):
    check = {}
    n= len(array)
    for i in range(n):
        element = target - array[i]
        if element in check:
            return [check[element],i]
        if array[i] not in check:
            check[array[i]] = i
         
    return None

print(twosum([2,7,11,15],9))     