# Problem: Find elemnet frequency
# Difficulty:Easy
# Topic: hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)

def element_freq(array,target):
    freq = {}
    for i in array:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq[target]

print(element_freq([1,2,2,3,2],2))            