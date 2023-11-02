def times_ten(start_index: int, end_index: int):
    result = {}
    for i in range(start_index, end_index+1):
        result[i] = i*10
    return result

def factorials(n: int):
    result = {}
    for i in range(1,n+1):
        factorial = 1
        for f in range(1,i+1):
            factorial *= f
        result[i] = factorial
    return result

def histogram(s: str):
    result = {}
    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    for k in sorted(result):
        print(f'{k} {"*"*result[k]}')

phone_book = {}
action = int(input('command (1 search, 2 add, 3 quit):'))
while action != 3:
    if action == 1:
        name = input('name:')
        if name in phone_book:
            print(phone_book[name])
        else:
            print('no number')
    elif action == 2:
        name = input('name:')
        number = input('number:')
        phone_book[name] = number
        print('ok!')
    action = int(input('command (1 search, 2 add, 3 quit):'))
print('quitting...')

phone_book = {}
action = int(input('command (1 search, 2 add, 3 quit):'))
while action != 3:
    if action == 1:
        name = input('name:')
        if name in phone_book:
            for num in phone_book[name]:
                print(num)
        else:
            print('no number')
    elif action == 2:
        name = input('name:')
        number = input('number:')
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(number)
        print('ok!')
    action = int(input('command (1 search, 2 add, 3 quit):'))
print('quitting...')

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({
        'name': name,
        'director': director,
        'year': year,
        'runtime': runtime
    })

def find_movies(database: list, search_term: str):
    result = []
    for movie in database:
        if search_term.lower() in movie['name'].lower():
            print('111')
            result.append(movie)
    return result



