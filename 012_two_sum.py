#Problem: Find Pair With Given Sum
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def find_sum(array,target):
    check = {}
    for i in array:
        element = target - i
        if element in check:
            return [check[element] ,i]
        check[i]=i
    return False    

print(find_sum([2,7,11,15],9))