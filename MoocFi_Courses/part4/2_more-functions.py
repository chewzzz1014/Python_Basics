def line(times, val):
    if val == '':
        print('*'*times)
    else:
        print(val[0]*times)

def line2(times, val):
    for i in range(times):
        print(val*10)

def square_of_hashes(size):
    line3(size, "#")
def line3(n, value):
    for i in range(n):
        print(value*n)

def triangle(size):
    line4(size, "#")
def line4(n, value):
    for i in range(1,n+1):
        print(i*value)

def shape(n1, v1, n2, v2):
    line5(n1,v1,n2,v2)
def line5(n1,v1,n2,v2):
    for i in range(1,n1+1):
            print(i*v1)
    for j in range(n2):
        print(n1*v2)

def spruce(n):
    print('a spruce!')
    current = 1
    for row in range(1,n+1):
        print(f'{" "*(n-row)}{"*"*current}')
        current += 2
    print(f'{" "*(n-1)}*')

def greatest_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c

def same_chars(val, n1, n2):
    if n1<len(val) and n2<len(val):
        return val[n1] == val[n2]
    else:
        return False

def first_word(val):
    return val.split(" ")[0]
def second_word(val):
    return val.split(" ")[1]
def last_word(val):
    return val.split(" ")[-1]



