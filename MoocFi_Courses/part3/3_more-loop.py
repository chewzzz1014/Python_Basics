n = int(input('Please type in a number:'))
i = 1
j = 1
while i <= n:
    while j <= n:
        print(f'{i} x {j} = {i*j}')
        j += 1
    i += 1
    j = 1

words = input('Please type in a sentence:')
for w in words.split(' '):
    print(w[0])

n = int(input('Please type in a number:'))
while n >= 1:
    factorial = 1
    current = 1
    while current <= n:
        factorial *= current
        current += 1
    print(f'The factorial of the number {n} is {factorial}')
    n = int(input('Please type in a number:'))
print('Thanks and bye!')

n = int(input('Please type in a number:'))
current = 1
while current<=n:
    v1 = current
    v2 = current+1
    if v2 > n:
        print(v1)
        break
    print(v2)
    print(v1)
    current = v2+1

n = int(input('Please type in a number:'))
currentFront = 1
currentBack = n
gap = 0
while True:
    v1 = currentFront + gap
    v2 = currentBack - gap
    if v1>n or v2<1:
        break
    else:
        print(v1)
        print(v2)
    gap += 1







