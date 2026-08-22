#problem: merge two array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def merge_arr(a,b):
    new_arr = []
    for i in a:
        new_arr.append(i)
    for i in b:
        new_arr.append(i)
    return new_arr

print(merge_arr([1,2,3],[4,5,6])) 
print(merge_arr([],[1,2]))
       