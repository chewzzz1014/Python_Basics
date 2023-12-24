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


