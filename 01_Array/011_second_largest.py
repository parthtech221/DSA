# Problem: find second largest element
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def second_large(arr):
    if len(arr) < 2:
        return None
    large = arr[0]
    s_large = None
    for i in arr:
        if large != i:
            if i > large :
                s_large = large
                large = i 
            if i < large:
                if s_large==None:
                    s_large = i
            if i < large:
                if i > s_large :
                    s_large = i 
        else:
            continue            
               
    if s_large == None:
        return None
    else:
        return s_large            
        
print(second_large([9, 9, 8, 7]))  


############# OR ###########
          
def second_larg(arr):
    if len(arr) < 2:
        return None

    largest = arr[0]
    second_largest = None

    for num in arr[1:]:

        if num > largest:
            second_largest = largest
            largest = num

        elif num != largest and (
            second_largest is None or num > second_largest
        ):
            second_largest = num

    return second_largest          
    