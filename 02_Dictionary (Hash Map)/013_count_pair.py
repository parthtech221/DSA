#Problem: Count Pairs With Given Sum
#Difficulty: Easy-Medium
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def count_pair(array,target):
    check = {}
    count = 0
    for i in array:
        element = target - i
        if element in check:
            count+=1
        check[i]=True
    return count

print(count_pair([1,5,7,-1,5],6))        