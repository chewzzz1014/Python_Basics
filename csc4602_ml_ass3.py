def calc_x(chromosome):
    current_idx = 4
    str_sum = 0
    for i in chromosome:
        if i == '0':
            pass
        if i == '1':
            str_sum += (2**current_idx)
        current_idx -= 1
    return (-5) + str_sum * (25/((2**5)-1))

def calc_fitness(x):
    return -(x**2) + (4*x) + 100

population_1 = ['01010', '10101', '10111']
population_2 = ['01101', '10010']
population_3 = ['01110', '10011']
population_4 = ['11100', '11110']

print('***********************')
for item in population_4:
    x = round(calc_x(item), 4)
    fx = round(calc_fitness(x), 4)
    print(f'{item}\nx = {x}\nf(x) = {fx}\n')