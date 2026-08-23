# problem: leaders in array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def leaders(arr):
    new_arr = []
    for i in range(len(arr)):
        count = 0
        for j in range(i+1,len(arr)):
            leader = True
            if arr[i]<arr[j]:
                leader = False
                break
        if leader==True and count==0:
            new_arr.append(arr[i])
            count+=1    
            
    return new_arr

print(leaders([20,16,13,17,4,3,5,2]))                       