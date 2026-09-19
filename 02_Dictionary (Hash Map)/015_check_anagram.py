#Problem: Check Anagram
#Difficulty: Easy
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def check_anagram(string1,string2):
    check = {}
    for i in string1:
        if i in check:
            check[i]+=1
        else:    
            check[i]=1
    for j in string2:
        if j not in check:
            return False
    return True

print(check_anagram("listen","silent"))            