#Problem: Find Common Elements
#Difficulty: Easy
#Topic: HashMap
#Time: O(n + m)
#Space: O(n)

def find_common(array1,array2):
    check = {}
    for i in array1:
        check[i]=True
    for j in array2:
        if j in check:
            return j  
    return False           
                
print(find_common([1,2,3,4],[3,4,5,6]))        