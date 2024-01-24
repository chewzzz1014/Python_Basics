def sort_by_remaining_stock(items: list):
    return sorted(items, key=lambda x:x[2])

def sort_by_seasons(items: list):
    return sorted(items, key=lambda x:x['seasons'])

def sort_by_ratings(items: list):
    return sorted(items, key=lambda x:x['rating'], reverse=True)

def sort_by_length(routes: list):
    return sorted(routes, key=lambda x:x.length, reverse=True)

def sort_by_difficulty(routes: list):
    def sort_grade(route):
        return (route.grade, route.length)
    return sorted(routes, key=sort_grade, reverse=True)

class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"


def sort_by_number_of_routes(areas):
    return sorted(areas, key=lambda x:x.routes())

def sort_by_most_difficult(areas):
    return sorted(areas, key=lambda x:x.hardest_route().grade, reverse=True)


class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(players):
    return sorted(players, key=lambda x:x.goals, reverse=True)[0].name

def most_points(players):
    player = sorted(players, key=lambda x:x.goals+x.passes, reverse=True)[0]
    return (player.name, player.number)

def least_minutes(players):
    return sorted(players, key=lambda x:x.minutes)[0]

def search(products: list, criterion: callable):
    return [x for x in products if criterion(x)]

