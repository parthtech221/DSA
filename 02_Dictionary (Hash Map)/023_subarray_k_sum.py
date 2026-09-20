#Problem: Longest Subarray With Sum K
#Difficulty: medium
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def subarray_sum(array , k):
    check = {}
    for i in array:
        if i not in check:
            check[i]=True
            