#Problem: Top K Frequent Elements
#Difficulty: medium
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def k_freq(array,k):
    check = {}
    new_array = []
    for i in array:
        if i not in check:
            check[i]=1
        else:
            check[i]+=1
        if (check[i]>= k) and (i not in new_array):
            new_array.append(i)
    return new_array
        
print(k_freq([1,1,1,2,2,3],2))                    