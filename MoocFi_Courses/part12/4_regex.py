import re


def is_dotw(my_string: str):
    week = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    return True if re.search(week, my_string) else False


def all_vowels(my_string: str):
    vowel = "^[aeiouAEIOU]+$"
    return True if re.search(vowel, my_string) else False


def time_of_day(my_string: str):
    time_24 = "^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$"
    return True if re.search(time_24, my_string) else False

