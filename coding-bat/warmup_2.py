def string_times(str, n):
  return str*n

def front_times(str, n):
  if len(str)<3:
    return str*n
  return str[:3]*n

def string_bits(str):
  result = ''
  for idx, ele in enumerate(str):
    if idx%2==0:
      result += ele
  return result

def string_splosion(str):
  result = ''
  for x in range(1, len(str)+1):
    result += str[:x]
  return result

def last2(str):
  target = str[-2:]
  count = 0
  for idx in range(0, len(str)-2):
    if str[idx:idx+2] == target:
      count += 1
  return count

def array_count9(nums):
  return len(filter(lambda x:x==9, nums))

def array_front9(nums):
  return 9 in nums[:4]

def array123(nums):
  for idx in range(len(nums)-2):
    if nums[idx]==1 and nums[idx+1]==2 and nums[idx+2]==3:
      return True
  return False

def string_match(a, b):
  count = 0
  for idx in range(min(len(a),len(b))-1):
    if a[idx:idx+2]==b[idx:idx+2]:
      count += 1
  return count