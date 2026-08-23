#problem: best time to bbuy and sell stock
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def buy_sell(arr):
    max = 0
    buy = None
    sell = None
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            diff = arr[j]-arr[i]
            if diff>max:
                max = diff
                buy=arr[i]
                sell=arr[j]
    return buy,sell,max

print(buy_sell([7, 1, 5, 3, 6, 4]))