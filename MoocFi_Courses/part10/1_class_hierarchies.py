# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed


class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self._weight = weight

    def __str__(self):
        return f'{self.model}, {self.speed} MHz, {self._weight} kg'


# TEE RATKAISUSI TÄHÄN:
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year


class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games


class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        return list(filter(lambda x: x.year < 1990, super().list_games()))


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, length: int):
        super().__init__(length, length)
    def __str__(self):
        return f"square {self.width}x{self.width}"


import random
import re


class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        return 0


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        v1 = re.sub(r'[^aeiouAEIOU]', '', player1_word)
        v2 = re.sub(r'[^aeiouAEIOU]', '', player2_word)
        if len(v1) > len(v2):
            return 1
        elif len(v1) < len(v2):
            return 2
        return 0


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        allowed = ['rock', 'paper', 'scissors']
        p1 = player1_word
        p2 = player2_word
        if p1 not in allowed and p2 not in allowed:
            return 0
        elif p1 not in allowed:
            return 2
        elif p2 not in allowed:
            return 1
        if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (
                p1 == 'scissors' and p2 == 'paper'):
            return 1
        elif p1 == p2:
            return 0
        else:
            return 2
