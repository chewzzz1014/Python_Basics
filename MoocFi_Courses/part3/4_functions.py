def seven_brothers():
    print('Aapo')
    print('Eero')
    print('Juhani')
    print('Lauri')
    print('Simeoni')
    print('Timo')
    print('Tuomas')

def first_character(text):
    print(text[0])

def mean(a, b, c):
    print((a+b+c)/3)

def print_many_times(text, times):
    for i in range(times):
        print(text)

def hash_square(n):
    for i in range(n):
        print('#'*n)

def chessboard(n):
    for i in range(n):
        result = ''
        if i==0 or i%2==0:
            result += '1'
        else:
            result += '0'
        for j in range(n-1):
            if result[-1] == '0':
                result += '1'
            else:
                result += '0'
        print(result)

def squared(x, n):
    for i in range(n):
        result = ''
        current_idx = 0
        for j in range(n):
            if j >= len(x):
                current_idx = 0
                result += x + x[:n-len(x)]
            else:
                result += x[j]
                current_idx += 1
        print(result)

