def lone_sum(a, b, c):
  if a==b and b==c:
    return 0
  elif a==b:
    return c
  elif a==c:
    return b
  elif b==c:
    return a
  return a+b+c


def lucky_sum(a, b, c):
  if a==13 and b==13 and c==13:
    return 0
  elif a==13:
    return 0
  elif b==13:
    return a
  elif c==13:
    return a+b
  return a+b+c


def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
  if 13 <= n <= 19 and n != 15 and n != 16:
    return 0
  return n


