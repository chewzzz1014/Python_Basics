import math

def square_roots(numbers: list):
    return [math.sqrt(x) for x in numbers]

def rows_of_stars(numbers: list):
    return ['*'*x for x in numbers]


class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')

def best_results(results: list):
    return [max(x.grade1, x.grade2, x.grade3) for x in results]

def lengths(lists: list):
    return [len(x) for x in lists]

def remove_smaller_than(numbers: list, limit: int):
    return [x for x in numbers if x>=limit]

def begin_with_vowel(words: list):
    return [x for x in words if x[0].lower() in ['a', 'e', 'i', 'o', 'u']]


class LotteryNumbers:
    def __init__(self, week_number: int, numbers: list):
        self.week_number = week_number
        self.numbers = numbers

    def number_of_hits(self, numbers: list):
        return len([x for x in numbers if x in self.numbers])

    def hits_in_place(self, numbers):
        return [x if x == self.numbers[idx] else -1 for idx, x in enumerate(numbers)]