num = 1
while num <= 30:
    if num%2 == 0:
        print(num)
    num += 1

limit = int(input('Upper limit:'))
current = 1
while current < limit:
    print(current)
    current += 1

limit = int(input('Upper limit:'))
current = 1
while current <= limit:
    print(current)
    current *= 2

limit = int(input('Upper limit:'))
base = int(input('Base:'))
current = 1
while current <= limit:
    print(current)
    current *= base

limit = int(input('limit:'))
current = 1
sum = 0
while sum < limit:
    sum += current
    current += 1
print(sum)

limit = int(input('limit:'))
current = 1
sum = 0
result = '1'
while sum < limit:
    sum += current
    if current > 1:
        result += f' + {current}'
    current += 1
print(f'{result} = {sum}')

