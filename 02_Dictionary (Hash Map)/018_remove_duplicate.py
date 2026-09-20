#Problem: remove Duplicate Element
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def remove_duplicate(array):
    check = {}
    new_array = []
    for i in array:
        if i not in check:
            check[i]= True
            new_array.append(i)           
    return new_array
print(remove_duplicate([1,2,2,3,1,4])) 
print(remove_duplicate([1,1,1,1])) 