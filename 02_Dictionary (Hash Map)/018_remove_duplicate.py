#Problem: remove Duplicate Element
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def remove_duplicate(array):
    check = {}
    for i in array:
        if i in check:
            array.remove(i)
        else:
            check[i]= True
    return array
print(remove_duplicate([1,2,2,3,1,4])) 