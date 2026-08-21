# Problem: find index of element
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def findindex(arr,target):
    index = -1
    for i in arr:
        index += 1
        if target==i:
            break
        else:
            return "not found"
    return index

print(findindex([10,20,30,40],5))    