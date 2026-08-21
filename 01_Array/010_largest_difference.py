# Problem: largest difference in array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def largediff(arr):
    max=arr[0]
    min=arr[0]
    for i in arr:
        if max<i:
            max=i
    for i in arr:
            if min>i:
                min=i 
    return max-min

print(largediff([2,10,5,1]))                   
        