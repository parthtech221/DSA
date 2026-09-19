#Problem: Character Frequency
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def charcter_freq(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

print(charcter_freq("banana"))           