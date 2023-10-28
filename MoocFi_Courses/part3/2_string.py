words = input('Please type in a string:')
times = int(input('Please type in an amount'))
print(words * times)

word1 = input('Please type in string 1:')
word2 = input('Please type in string 2:')
if len(word1) > len(word2):
    print(f'{word1} is longer')
elif len(word1) < len(word2):
    print(f'{word2} is longer')
else:
    print('The strings are equally long')

words = input('Please type in a string:')
current = len(words) - 1
while current >= 0:
    print(words[current])
    current -= 1

words = input('Please type in a string:')
if words[1] != words[-2]:
    print('The second and the second to last characters are different')
else:
    print(f'The second and the second to last characters are {words[1]}')

length = int(input('Width:'))
print('#' * length)

length = int(input('Width:'))
height = int(input('Height'))
for i in range(height):
    print('#' * length)

words = input('Please type in a string:')
while words != '':
    print(words)
    print('-' * len(words))
    words = input('Please type in a string:')

words = input('Please type in a string:')
if len(words)<20:
    print(f'{"*"* (20-len(words))}{words}')
else:
    print(words)

words = input('Word:')
print('*'*30)
if len(words)%2==0:
    print(f'*{((28-len(words))//2) * " "}{words}{((28-len(words))//2) * " "}*')
else:
    print(f'*{((28 - len(words)) // 2) * " "}{words}{((28 - len(words)) // 2) * " "} *')
print('*'*30)

words = input('Please type in a string:')
for i in range(len(words)+1):
    print(words[:i])

words = input('Please type in a string:')
for i in range(len(words),-1,-1):
    print(words[i:])

words = input('Please type in a string:')
for x in ['a','e','o']:
    if x in words:
        print(f'{x} found')
    else:
        print(f'{x} not found')

words = input('Please type in a word:')
target = input('Please type in a character:')
if words.find(target) != -1 and words.find(target)+3<=len(words):
    print(words[words.find(target):words.find(target)+3])

words = input('Please type in a word:')
target = input('Please type in a character:')
current = words.find(target)
while current+3<=len(words):
    if words[current] == target:
        print(words[current:current+3])
    current += 1

words = input('Please type in a word:')
target = input('Please type in a character:')
current = words.find(target)
occurence = 1
while current+len(target)<=len(words) and occurence<=2:
    if words[current] == target and words[current:current+len(target)] == target:
        print(words[current:current+len(target)])
        occurence+=1
        if occurence == 2:
            break
        current += len(target)
    else:
        current += 1
if occurence == 2:
    print(f'The second occurrence of the substring is at index {current}.')
else:
    print('The substring does not occur twice in the string.')


