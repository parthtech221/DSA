def freq_count(arry):
    freq = {}
    for i in arry:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1 
    return freq

print(freq_count([1,2,2,3,2,1]))           