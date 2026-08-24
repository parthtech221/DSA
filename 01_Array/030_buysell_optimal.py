# problem: Buy and sell stock in O(n)
# Difficulty: Easy
# Topic: Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)

def buy_sell(arr):
    minimum_price = arr[0]
    maximum_profit = 0
    profit = 0
    for i in range(len(arr)):
        
        if arr[i]<minimum_price:
            minimum_price=arr[i]
        profit=arr[i]-minimum_price 
        if profit>maximum_profit:
            maximum_profit = profit
    return maximum_profit         
           
print(buy_sell([7,1,5,3,6,4]))
print(buy_sell([8,2,3,7,9,1,5]))           