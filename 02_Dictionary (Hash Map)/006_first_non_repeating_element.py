# Problem: first non repeating element
# Difficulty:Easy
# Topic: hashmap
# Time Complexity: O(n+m)
# Space Complexity: O(n)

def frist_non_reapeting(array):
    check = {}
    for i in array:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1 
    for i in array:
        if check[i]==1:
            return i               
    
print(frist_non_reapeting([2, 5, 1, 2, 3, 5])) 