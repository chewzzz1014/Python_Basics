def everything_reversed(my_list):
    result = []
    for i in my_list[::-1]:
        result.append(i[::-1])
    return result

def most_common_character(s):
    max_occur = 0
    max_occur_ele = ''
    for i in s:
        if s.count(i)>max_occur:
            max_occur = s.count(i)
            max_occur_ele = i
    return max_occur_ele

def no_vowels(s):
    result = s
    for i in 'aeiou':
        result = result.replace(i, '')
    return result

def no_shouting(my_list):
    result = []
    for i in my_list:
        if not i.isupper():
            result.append(i)
    return result

