class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

def fastest_car(cars: list) :
    min_car = cars[0]
    for car in cars:
        if car.top_speed > min_car.top_speed:
            min_car = car
    return min_car.make

##############################################################################################

class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

# # WRITE YOUR SOLUTION HERE:
def passed(submissions: list, lowest_passing: int):
    return list(filter(lambda x:x.points >= lowest_passing, submissions))

##############################################################################################
class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        self.number_of_weigh_ins += 1
        return person.weight

    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.number_of_weigh_ins

##############################################################################################
# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment < 2.5:
            return payment
        self.funds += 2.5
        self.lunches += 1
        return payment - 2.5

    def eat_special(self, payment: float):
        if payment < 4.3:
            return payment
        self.funds += 4.3
        self.specials += 1
        return payment - 4.3

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >= 2.5:
            self.lunches += 1
            return card.subtract_from_balance(2.5)
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance >= 4.3:
            self.specials += 1
            return card.subtract_from_balance(4.3)
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)


##############################################################################################
# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to: 'RealProperty'):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to: 'RealProperty'):
        return abs(self.price_per_sqm * self.square_metres - compared_to.price_per_sqm * compared_to.square_metres)

    def more_expensive(self, compared_to: 'RealProperty'):
        return (self.price_per_sqm * self.square_metres) > (compared_to.price_per_sqm * compared_to.square_metres)