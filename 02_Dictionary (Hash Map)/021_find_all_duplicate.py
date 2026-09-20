#Problem: Find all duplicates
#Difficulty: medium
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def all_duplicate(array):
    check = {}
    new_array = []
    for i in array:
        if i not in check:
            check[i]=1
        else:
            check[i]+=1    
        if check[i]==2:
            new_array.append(i)
    return new_array

print(all_duplicate([1,2,3,2,4,1,5]))            