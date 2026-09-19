#Problem: Check If Two Arrays Have Common Element
#Difficulty: Easy
#Topic: HashMap
#Time: O(n + m)
#Space: O(n)

def common_element(arr1,arr2):
    check = {}
    for i in arr1:
        check[i]=True
    for j in arr2:
        if j in check:
            return True
        
    return False
 
print(common_element([1,2,3],[5,6,3]))            