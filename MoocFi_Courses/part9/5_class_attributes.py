class City:
    postcodes = {'Helsinki': '00100', 'Turku': '20100', 'Tampere': '33100', 'Rovaniemi': '96100', 'Oulu': '90100'}

    def __init__(self, name: str, population: int):
        self.__name = name
        self.__population = population

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    def __str__(self):
        return f"{self.__name} ({self.__population} residents.)"


class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        results = {}
        for n in my_list:
            if n not in results:
                results[n] = 1
            else:
                results[n] += 1
        max_occur = 0
        max_occur_item = 0
        for n in results:
            if results[n] > max_occur:
                max_occur = results[n]
                max_occur_item = n
        return max_occur_item

    @classmethod
    def doubles(clas, my_list: list):
        results = {}
        for n in my_list:
            if n not in results:
                results[n] = 1
            else:
                results[n] += 1
        return len(list(filter(lambda x: x >= 2, results.values())))


# numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))