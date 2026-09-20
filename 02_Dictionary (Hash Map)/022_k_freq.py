# Problem: Top K Frequent Elements
# Difficulty: Medium
# Topic: HashMap
# Time Complexity: O(n + k*n)
# Space Complexity: O(n)

def k_freq(array, k):

    check = {}
    result = []

    # Build frequency map
    for i in array:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1

    # Find top k elements
    while len(result) < k and len(check) > 0:

        max_freq = 0
        max_key = None

        for key in check:
            if check[key] > max_freq:
                max_freq = check[key]
                max_key = key

        result.append(max_key)
        del check[max_key]

    return result


print(k_freq([1,1,1,2,2,3,3,3,3], 2))