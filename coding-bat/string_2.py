def double_char(str):
  return "".join(list(map(lambda x:x*2, list(str))))

def count_hi(str):
  count = 0
  for idx in range(len(str)):
    if str[idx:idx+2]=='hi':
      count+=1
  return count

def cat_dog(str):
  return str.count('dog') == str.count('cat')

def count_code(str):
  count = 0
  for idx in range(len(str)-3):
    if str[idx:idx+2]=='co' and str[idx+3]=='e':
      count += 1
  return count


def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (a in b and b[-1 * len(a):] == a) or (b in a and a[-1 * len(b):] == b)

def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i:i+3] == "xyz" and (i == 0 or str[i-1] != '.'):
      return True
  return False
