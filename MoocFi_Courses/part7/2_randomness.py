from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    return shuffle(number_pool)[:amount]

