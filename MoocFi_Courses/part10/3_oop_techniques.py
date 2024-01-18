# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__value = self.__euros + self.__cents / 100

    def __str__(self):
        return f"{self.__euros + self.__cents / 100:.2f} eur"

    def __eq__(self, another):
        return self.__value == (another.__euros + another.__cents / 100)

    def __lt__(self, another):
        return self.__value < (another.__euros + another.__cents / 100)

    def __gt__(self, another):
        return self.__value > (another.__euros + another.__cents / 100)

    def __ne__(self, another):
        return self.__value != (another.__euros + another.__cents / 100)

    def __add__(self, another):
        return Money(self.__euros + another.__euros, self.__cents + another.__cents)

    def __sub__(self, another):
        if self.__value < another.__value:
            raise ValueError('a negative result is not allowed')
        return Money(self.__euros - another.__euros, self.__cents - another.__cents)


# TEE RATKAISUSI TÄHÄN:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < len(self.products):
            item = self.products[self.n]
            self.n += 1
            return item
        else:
            raise StopIteration
