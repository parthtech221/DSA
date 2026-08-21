# Problem: count frequency
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def freqcount(arr,target):
    count = 0 
    for i in arr:
        if i==target:
            count += 1
    return count

print(freqcount([1,2,2,3,2],2))        