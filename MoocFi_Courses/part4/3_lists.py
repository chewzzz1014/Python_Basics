my_list = [1,2,3,4,5]
idx = int(input('Index:'))
while idx != -1:
    value = int(input('New value:'))
    my_list[idx] = value
    print(my_list)
    idx = int(input('Index:'))

my_list = []
n = int(input('How many items:'))
for i in range(n):
    val = int(input(f'Item {i+1}:'))
    my_list.append(val)
print(my_list)

my_list = []
print(f'The list is now {my_list}')
action = input('a(d)d, (r)emove or e(x)it:')
while action != 'x':
    if len(my_list)>0:
        current = my_list[-1]
    else:
        current = 0
    if action == 'd':
        my_list.append(current+1)
    elif action == 'r':
        my_list.pop()
    current += 1
    print(f'The list is now {my_list}')
    action = input('a(d)d, (r)emove or e(x)it:')
print('Bye!')

my_list = []
word = input('Word:')
while word not in my_list:
    my_list.append(word)
    word = input('Word:')
print(f'You typed in {len(my_list)} different words')

my_list = []
n = int(input('New item:'))
while n != 0:
    my_list.append(n)
    print(f'The list now: {my_list}')
    print(f'The list in order: {sorted(my_list)}')
    n = int(input('New item:'))
print('Bye!')

def length(my_list):
    return len(my_list)

def mean(my_list):
    return sum(my_list)/len(my_list)

def range_of_list(my_list):
    return max(my_list) - min(my_list)















