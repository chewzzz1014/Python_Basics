import math

def hypotenuse(leg1: float, leg2: float):
    return math.sqrt(leg1**2 + leg2**2)

def smallest_average(person1: dict, person2: dict, person3: dict):
    sum_1 = sum(list(filter(lambda x: str(x).isdigit(), person1.values())))
    sum_2 = sum(list(filter(lambda x: str(x).isdigit(), person2.values())))
    sum_3 = sum(list(filter(lambda x: str(x).isdigit(), person3.values())))
    if sum_1<sum_2 and sum_1<sum_3:
        return person1
    elif sum_2<sum_1 and sum_2<sum_3:
        return person2
    else:
        return person3

#############################################################################

def row_sums(my_matrix: list):
    my_matrix = [row.append(sum(row)) for row in my_matrix]


#############################################################################
