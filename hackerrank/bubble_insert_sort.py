def bubble_sort(arr):
    nums = arr[:]
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

def insertion_sort(arr):
    nums = arr[:]
    for i in range(len(nums)):
        current = nums.pop(i)
        j = i-1
        while j>=0 and nums[j]>current:
            j -= 1
        nums.insert(j+1, current)
    return nums