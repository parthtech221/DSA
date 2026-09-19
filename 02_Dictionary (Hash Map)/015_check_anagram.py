#Problem: Check Anagram
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def check_anagram(string1,string2):
    checki = {}
    checkj = {}
    for i in string1:
        if i in checki:
            checki[i]+=1
        else:    
            checki[i]=1
    for j in string2:
        if j in checkj:
            checkj[j]+=1
        else:
            checkj[j]=1    
    return checki==checkj

print(check_anagram("listen","silent"))            