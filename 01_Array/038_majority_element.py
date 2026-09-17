# problem: majority element with time o(n)
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def majority(array):
    check = {}
    for i in array:
        if i in check:
            check[i] += 1
        else:
            check[i]=1
        if check[i] > len(array)//2:
            return i
    
print(majority([2,2,1,1,1,2,2]))                