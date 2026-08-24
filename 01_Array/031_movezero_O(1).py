# problem: move zero to end O(1) space
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def movexero(arr):
    n=len(arr)
    previous = 0
    for i in range(1,n-1):
        if arr[previous]!=0 and arr[i]==0:
            previous+=1
        if arr[previous]==0 and arr[i]!=0:
            arr[i],arr[previous]=arr[previous],arr[i]
    return arr
                
print(movexero([1,0,2,0,3,0]))        