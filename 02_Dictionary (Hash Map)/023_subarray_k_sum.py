#Problem: Longest Subarray With Sum K
#Difficulty: medium
#Topic: HashMap
#Time: O(n)
#Space: O(n)

def subarray_sum(array, k):

    max_length = 0

    for i in range(len(array)):

        current_sum = 0

        for j in range(i, len(array)):

            current_sum += array[j]

            if current_sum == k:

                length = j - i + 1

                if length > max_length:
                    max_length = length

    return max_length
print(subarray_sum([1, -1, 5, -2, 3],3))            