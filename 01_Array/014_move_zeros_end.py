# Problem: move all zero to end
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def move_zero(arr):
    count = 0
    new_arr = []
    for i in arr:
        if i != 0 :
            new_arr.append(i)
        else:
            count += 1
    for i in range(count):
        new_arr.append(0)
    return new_arr   

print(move_zero([1, 0, 2, 0, 3, 0]))             