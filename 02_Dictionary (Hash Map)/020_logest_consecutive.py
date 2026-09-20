#Problem: Longest Consecutive Sequence
#Difficulty: medium
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def longest_sequence(array):
    check = {}
    max_length = 0
    for i in array:
        check[i]=True
    for i in array:    
        if (i-1) not in check:
            current = i
            length = 1
            while (current +1) in check:
                current += 1
                length += 1
            if length > max_length:
                max_length = length   

    return max_length

print(longest_sequence([100,4,200,1,3,2]))                   