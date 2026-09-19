#Problem: Find Highest Frequency Count
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def highest_freq(array):
    check = {}
    highest = 0
    for i in array:
        if i in check:
            check[i]+=1
        else:    
            check[i]=1
        if check[i]>highest:
            highest = check[i]
    return highest

print(highest_freq([1,2,2,3,2,1,2]))        