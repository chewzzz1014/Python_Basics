def create_tuple(x: int, y: int, z: int):
    return (min([x,y,z]), max([x,y,z]), sum([x,y,z]))

def oldest_person(people: list):
    oldest = people[0][1]
    oldest_name = people[0][0]
    for p in people:
        print(p[0])
        if (2023-p[1])>(2023-oldest):
            oldest = p[1]
            oldest_name = p[0]
    return oldest_name

def older_people(people: list, year: int):
    result = []
    for p in people:
        if p[1]<year:
            result.append(p[0])
    return result

