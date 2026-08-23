# problem: leaders in array
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def leaders(arr):
    new_arr = []
    for i in range(len(arr)):
        leader = True
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                leader = False
                break
        if leader==True :
            new_arr.append(arr[i])   
      
    return new_arr

print(leaders([20,16,13,17,4,3,5,2]))                       