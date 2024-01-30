def even_numbers(beginning: int, maximum: int):
    start_idx = beginning if beginning%2==0 else beginning+1
    for x in range(start_idx, maximum+1, 2):
        yield x


def prime_numbers():
    current = 2
    while True:
        is_prime = True
        for x in range(2, current-1):
            if current%x==0:
                is_prime = False
                break
        if is_prime:
            yield current
        current += 1

import random

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        start_idx = random.randint(0,len(characters))
        yield characters[start_idx:start_idx+length]

        