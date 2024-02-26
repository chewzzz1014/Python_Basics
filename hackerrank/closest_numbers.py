def closestNumbers(arr):
    arr.sort()
    min_diff = max(arr)
    pairs = []

    for i in range(len(arr) - 1):
        min_diff = min(min_diff, arr[i + 1] - arr[i])
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min_diff:
            pairs.append(arr[i])
            pairs.append(arr[i + 1])
    return pairs