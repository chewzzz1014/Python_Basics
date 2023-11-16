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

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
students = {}
grades = {}
with open(student_info) as rf:
    for line in rf:
        parsed_values = line.replace('\n', '').split(';')
        if parsed_values[0] == 'id':
            continue
        else:
            students[parsed_values[0]] = parsed_values[1] + ' ' + parsed_values[2]

with open(exercise_data) as rf:
    for line in rf:
        parsed_values = line.replace('\n', '').split(';')
        if parsed_values[0] == 'id':
            continue
        else:
            student_id = parsed_values[0]
            grades[student_id] = []
            for i in range(1, len(parsed_values)):
                grades[student_id].append(int(parsed_values[i]))
for id, name in students.items():
    print(f'{name} {sum(grades[id])}')

import math
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = 'exam_points1.csv'
students = {}
points = {}
with open(student_info) as rf:
    for line in rf:
        parsed_values = line.replace('\n', '').split(';')
        if parsed_values[0] == 'id':
            continue
        else:
            students[parsed_values[0]] = parsed_values[1] + ' ' + parsed_values[2]
            points[parsed_values[0]] = []
# read exercise point
with open(exercise_data) as rf:
    for line in rf:
        parsed_values = line.replace('\n', '').split(';')
        if parsed_values[0] == 'id':
            continue
        else:
            student_id = parsed_values[0]
            total_completion = 0
            total_points = 0
            for i in range(1, len(parsed_values)):
                total_completion += int(parsed_values[i])

            total_points = math.floor(total_completion / 40 * 10)
            points[student_id].append(total_points)
# read exam point
with open(exam_data) as rf:
    for line in rf:
        parsed_values = line.replace('\n', '').split(';')
        if parsed_values[0] == 'id':
            continue
        else:
            student_id = parsed_values[0]
            total_points = 0
            for i in range(1, len(parsed_values)):
                total_points += int(parsed_values[i])
            points[student_id].append(total_points)
# print(points)
def get_grade(points):
    if 0<=points<=14:
        return 0
    elif 15<=points<=17:
        return 1
    elif 18<=points<=20:
        return 2
    elif 21<=points<=23:
        return 3
    elif 24<=points<=27:
        return 4
    elif points>=28:
        return 5
for id, name in students.items():
    print(f'{name} {get_grade(sum(points[id]))}')

