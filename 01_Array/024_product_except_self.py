#problem: product of array except self
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def produc_exceptself(arr):
    new_arr = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i!=j:
                product*=arr[j]
        new_arr.append(product)  
    return new_arr
      
print((produc_exceptself([1,2,3,4])))                  