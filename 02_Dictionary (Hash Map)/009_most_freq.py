# Problem: Find most frequent element
# Difficulty:Easy
# Topic: hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)

def most_frequent(array):
    freq = {}
    max = 0
    for i in array:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
            
        if freq[i]>max:
            max = freq[i]
    return max        

print(most_frequent([1,2,2,3,2]))