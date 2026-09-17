# Problem: count distinct element
# Difficulty:Easy
# Topic: hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)

def count_distinct(array):
    count = 0
    check = {}
    for i in array:
        if i not in check:
            check[i]=1
            count+=1
    return count

print(count_distinct([1,2,2,3,1,4]))        