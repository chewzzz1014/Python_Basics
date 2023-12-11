class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    def __str__(self):
        return f'{self.minutes:02}:{self.seconds:02}'
    def tick(self):
        if self.seconds==59:
            self.seconds = 0
            if self.minutes==59:
                self.minutes = 0
            else:
                self.minutes += 1
        else:
            self.seconds += 1
###############################################################################

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
    def tick(self):
        if self.seconds==59:
            self.seconds = 0
            if self.minutes==59:
                self.minutes = 0
                if self.hours==23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

###############################################################################

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f'The balance is {self.balance:.1f} euros'

    def eat_lunch(self):
        if self.balance - 2.6 >= 0:
            self.balance -= 2.6

    def eat_special(self):
        if self.balance - 4.6 >= 0:
            self.balance -= 4.6

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError('You cannot deposit an amount of money less than zero')
        else:
            self.balance += amount


peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
peters_card.deposit_money(20)
graces_card.eat_special()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')

###############################################################################
class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    def __str__(self):
        genres_list = ", ".join(self.genres)
        num_ratings = len(self.ratings)
        if num_ratings>0:
            avg_ratings = sum(self.ratings)/len(self.ratings)
            return f'{self.title} ({self.seasons} seasons)\ngenres: {genres_list}\n{num_ratings} ratings, average {round(avg_ratings, 1)} points'
        else:
            return f'{self.title} ({self.seasons} seasons)\ngenres: {genres_list}\nno ratings'
    def rate(self, rating: int):
        self.ratings.append(rating)

def minimum_grade(rating: float, series_list: list):
        return list(filter(lambda x:sum(x.ratings)>=rating,series_list))
def includes_genre(genre: str, series_list: list):
        return list(filter(lambda x: genre in x.genres,series_list))