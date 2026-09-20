#Problem: Find Duplicate Element
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def duplicate(array):
    check = {}
    for i in array:
        if i in check:
            return i
        else:
            check[i]= True
    return False
print(duplicate([1,2,3,4,2])) 