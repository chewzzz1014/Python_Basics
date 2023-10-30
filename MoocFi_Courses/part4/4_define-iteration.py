words = input('Please type in a string:')
for w in words:
    print(f'{w}')
    print('*')

n = int(input('Please type in a positive integer:'))
for i in range(n*-1, n+1):
    if i != 0:
        print(i)

def list_of_stars(my_list):
    for i in my_list:
        print('*'*i)

def anagrams(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    return ''.join(sorted_s1) == ''.join(sorted_s2)

def palindromes(s):
    if (len(s) / 2) % 2 != 0:
        mid = len(s) // 2
    else:
        mid = len(s) / 2
    for i in range(int(mid)):
        if s[i] != s[(i + 1) * -1]:
            return False
    return True
words = input('Please type in a palindrome:')
while not palindromes(words):
    print('that wasn\'t a palindrome')
    words = input('Please type in a palindrome:')
print(f'{words} is a palindrome!')

def sum_of_positives(my_list):
    sum = 0
    for i in my_list:
        if i>0:
            sum += i
    return sum

def even_numbers(my_list):
    result = []
    for i in my_list:
        if i%2 == 0:
            result.append(i)
    return result

def list_sum(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return result

def distinct_numbers(my_list):
    result = []
    for i in sorted(my_list):
        if i not in result:
            result.append(i)
    return result

def length_of_longest(my_list):
    max = 0
    for i in my_list:
        if len(i)>max:
            max = len(i)
    return max

def shortest(my_list):
    shortest_ele = my_list[0]
    for i in range(1, len(my_list)):
        if len(my_list[i])<len(shortest_ele):
            shortest_ele = my_list[i]
    return shortest_ele

def all_the_longest(my_list):
    longest_ele = ''
    result = []
    for ele in my_list:
        if len(ele)>=len(longest_ele):
            longest_ele = ele
    for ele in my_list:
        if len(ele) == len(longest_ele):
            result.append(ele)
    return result







