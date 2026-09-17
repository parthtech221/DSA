# Problem: first repeating element
# Difficulty:Easy
# Topic: hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)

def fristreapeting(array):
    check = {}
    for i in array:
        if i in check:
            return i
        else:
            check[i]= True
    return False
print(fristreapeting([2, 5, 1, 2, 3, 5])) 