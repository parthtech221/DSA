# problem: Find duplicate with time o(n)
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def duplicate(array):
    check = {}
    for i in array:
        if i in check:
            return True
        else:
            check[i]= "yes"
    return False
print(duplicate([1,2,3,4,5,5]))        