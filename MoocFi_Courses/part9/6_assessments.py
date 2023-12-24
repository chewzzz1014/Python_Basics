class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def weight(self):
        return self._weight

    def name(self):
        return self._name

    def __str__(self):
        return f'{self._name} ({self._weight} kg)'


class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.remaining_weight = max_weight
        self.items = []

    def add_item(self, item: Item):
        if item.weight() <= self.remaining_weight:
            self.remaining_weight -= item.weight()
            self.items.append(item)

    def __str__(self):
        return f'{len(self.items)} item{"s" if len(self.items) != 1 else ""} ({self.max_weight - self.remaining_weight} kg)'

    def print_items(self):
        for i in self.items:
            print(i)

    def weight(self):
        return sum(list(map(lambda x: x.weight(), self.items)))

    def heaviest_item(self):
        max_weight = max(list(map(lambda x: x.weight(), self.items)))
        return list(filter(lambda x: x.weight() >= max_weight, self.items))[0]


class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.remaining_weight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        sum_weight = sum(list(map(lambda x: x.weight(), suitcase.items)))
        if sum_weight <= self.remaining_weight:
            self.remaining_weight -= sum_weight
            self.suitcases.append(suitcase)

    def __str__(self):
        return f'{len(self.suitcases)} suitcase{"s" if len(self.suitcases) != 1 else ""}, space for {self.remaining_weight} kg'

    def print_items(self):
        for s in self.suitcases:
            s.print_items()