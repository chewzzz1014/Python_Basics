class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value>0:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial_value


class Person:
    def __init__(self, name):
        self.name = name

    def return_first_name(self):
        return self.name.split(' ')[0]

    def return_last_name(self):
        return self.name.split(' ')[1]


# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.count_numbers()>0:
            return self.get_sum()/self.count_numbers()
        else:
            return 0


ns_all = NumberStats()
ns_even = NumberStats()
ns_odd = NumberStats()

print('Please type in integer numbers:')
num = int(input())
while num != -1:
    ns_all.add_number(num)
    if num%2 == 0:
        ns_even.add_number(num)
    else:
        ns_odd.add_number(num)
    num = int(input())
print(f'Sum of numbers: {ns_all.get_sum()}')
print(f'Mean of numbers: {ns_all.average()}')
print(f'Sum of even numbers: {ns_even.get_sum()}')
print(f'Sum of odd numbers: {ns_odd.get_sum()}')