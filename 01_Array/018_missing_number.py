#problem: missing number
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def missing_num(arr):
    count = 1
    for i in arr:
        if i != count :
            return count
        count+=1
    return "no missing number"
 
print(missing_num([1,2,3,4,]))              