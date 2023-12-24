# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup(SuperHero):
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []
    @property
    def name(self):
        return self._name
    @property
    def location(self):
        return self._location
    def add_member(self, hero:SuperHero):
        self._members.append(hero)
    def print_group(self):
        print(f'Members: \n{"\n".join(list(map(str, self._members)))}')


class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        self.__password = password
        super().__init__(name)
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if self.__password != password:
            raise ValueError("Wrong password!")
        super().add_ingredient(ingredient, amount)
    def print_recipe(self, password: str):
        if self.__password != password:
            raise ValueError("Wrong password!")
        super().print_recipe()


