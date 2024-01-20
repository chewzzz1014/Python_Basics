def cigar_party(cigars, is_weekend):
  return (not is_weekend and 40<=cigars<=60) or (is_weekend and cigars>=40)

def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  return 1

def squirrel_play(temp, is_summer):
  return (not is_summer and 60<=temp<=90) or (is_summer and 60<=temp<=100)


def caught_speeding(speed, is_birthday):
  if (not is_birthday and speed<=60) or (is_birthday and speed<=65):
    return 0
  elif (not is_birthday and 61<=speed<=80) or (is_birthday and 66<=speed<=85):
    return 1
  elif (not is_birthday and speed>=81) or (is_birthday and speed>=86):
    return 2

def sorta_sum(a, b):
  if 10<=(a+b)<=19:
    return 20
  return a+b

def alarm_clock(day, vacation):
  is_weekend = day in [0,6]
  if (is_weekend and not vacation) or (not is_weekend and vacation):
    return '10:00'
  elif not is_weekend and not vacation:
    return '7:00'
  return 'off'


def love6(a, b):
  return a==6 or b==6 or a+b==6 or abs(a-b)==6

def in1to10(n, outside_mode):
  return (not outside_mode and 1<=n<=10) or (outside_mode and (n<=1 or n>=10))


