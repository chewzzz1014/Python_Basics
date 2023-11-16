def largest():
    max = 0
    with open('numbers.txt') as read_file:
        for line in read_file:
            n = int(line.replace('\n', ''))
            if n > max:
                max = n
    return max

def read_fruits():
    result = {}
    with open('fruits.csv') as read_file:
        for line in read_file:
            items_info = line.replace('\n', '').split(';')
            result[items_info[0]] = float(items_info[1])
    return result

def parse_numbers(line):
    result = line.replace('\n', '').split(',')
    for i in range(len(result)):
        result[i] = int(result[i])
    return result

def matrix_sum():
    total = 0
    with open('matrix.txt') as lines:
        for line in lines:
            numbers = parse_numbers(line)
            total += sum(numbers)
    return total
def matrix_max():
    max = 0
    with open('matrix.txt') as lines:
        for line in lines:
            numbers = parse_numbers(line)
            for n in numbers:
                if n > max:
                    max = n
    return max
def row_sums():
    result = []
    with open('matrix.txt') as lines:
        for line in lines:
            numbers = parse_numbers(line)
            result.append(sum(numbers))
    return result

