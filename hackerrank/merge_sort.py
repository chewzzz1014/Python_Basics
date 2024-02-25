def merge_sort(arr):
    nums = list(arr)
    mid = len(nums) // 2
    merge_l, merge_r = merge_sort(nums[:mid]), merge_sort(nums[mid:])
    sorted_nums = combine(merge_l, merge_r)
    return sorted_nums

def combine(arr1, arr2):
    idx1, idx2 = 0, 0
    merged = []
    while idx1<len(arr1) and idx2<len(arr2):
        if arr1[idx1]<arr2[idx2]:
            merged.append(arr1[idx1])
            idx1 += 1
        else:
            merged.append(arr2[idx2])
            idx2 += 1
    return merged + arr1[idx1:] + arr2[idx2:]