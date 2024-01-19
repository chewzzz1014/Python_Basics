def count_evens(nums):
  return len(list(filter(lambda x:x%2==0, nums)))

def big_diff(nums):
  return max(nums)-min(nums)

def centered_average(nums):
  total = 0
  count = 0
  min_val = min(nums)
  max_val = max(nums)
  has_skipped_min = False
  has_skipped_max = False
  for x in nums:
    if x==min_val and not has_skipped_min:
        has_skipped_min = True
        continue
    if x==max_val and not has_skipped_max:
        has_skipped_max = True
        continue
    total += x
    count += 1
  return total//count


def sum13(nums):
  total = 0
  idx = 0
  if len(nums)==0:
    return 0
  while idx < len(nums):
    if nums[idx]==13:
      idx += 1
    else:
      total += nums[idx]
    idx += 1
  return total


def has22(nums):
  has_prev = -1
  for idx in range(len(nums)):
    if nums[idx]==2 and has_prev==-1:
      has_prev = idx
    elif nums[idx]==2 and has_prev==idx-1:
      return True
    else:
      has_prev=-1
  return False
