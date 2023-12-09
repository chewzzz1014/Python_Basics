class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


class Checklist:
    def __init__(self, header, entries):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id, balance, discount):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model, length, max_speed, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional

########################################################################################################

class Pet:
    def __init__(self, name, species, year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name: str, species: str, year_of_birth: int):
    return Pet(name, species, year_of_birth)

########################################################################################################
def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f'{book1.name} is older, it was published in {book1.year}')
    elif book1.year > book2.year:
        print(f'{book2.name} is older, it was published in {book2.year}')
    else:
        print(f'{book1.name} and {book2.name} were published in {book1.year}')

########################################################################################################
def books_of_genre(books: list, genre: str):
    return [book for book in books if book.genre == genre]