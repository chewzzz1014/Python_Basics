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
# points = {}
info = {}


def get_grade(points):
    if 0 <= points <= 14:
        return 0
    elif 15 <= points <= 17:
        return 1
    elif 18 <= points <= 20:
        return 2
    elif 21 <= points <= 23:
        return 3
    elif 24 <= points <= 27:
        return 4
    elif points >= 28:
        return 5


with open(student_info) as rf:
    for line in rf:
        parsed_values = line.replace('\n', '').split(';')
        if parsed_values[0] == 'id':
            continue
        else:
            students[parsed_values[0]] = parsed_values[1] + ' ' + parsed_values[2]
            # points[parsed_values[0]] = []
            info[parsed_values[0]] = {}
            info[parsed_values[0]]['name'] = students[parsed_values[0]]

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
            info[student_id]['exec_nbr'] = total_completion
            info[student_id]['exec_pts.'] = total_points
            # points[student_id].append(total_points)

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

            info[student_id]['exm_pts.'] = total_points
            info[student_id]['tot_pts.'] = info[student_id]['exec_pts.'] + info[student_id]['exm_pts.']
            info[student_id]['grade'] = get_grade(info[student_id]['tot_pts.'])
            # points[student_id].append(total_points)

# print(points)
cols = ['name', 'exec_nbr', 'exec_pts.', 'exm_pts.', 'tot_pts.', 'grade']
print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")

for id, name in students.items():
    current_info = info[id]
    print(
        f'{current_info[cols[0]]:22}{current_info[cols[1]]:10}{current_info[cols[2]]:10}{current_info[cols[3]]:10}{current_info[cols[4]]:10}{current_info[cols[5]]:10}')

#################################################

with open('wordlist.txt') as rf:
    words_list = []
    for line in rf:
        words_list.append(line.replace('\n', ''))

    user_word = input('Write text:')
    result = ''
    for w in user_word.split(' '):
        if w.lower() not in words_list:
            result += f'*{w}* '
        else:
            result += f'{w} '
    print(result)

#################################################

def search_by_name(filename: str, word: str):
    foods = []
    with open(filename) as rf:
        is_before_food_name = True
        for line in rf:
            parsed_line = line.replace('\n', '')
            if is_before_food_name and word.lower() in parsed_line.lower():
                foods.append(parsed_line)
            if parsed_line == '':
                is_before_food_name = True
            else:
                is_before_food_name = False
    return foods

def search_by_time(filename: str, prep_time: int):
    foods = {}
    with open(filename) as rf:
        lines = rf.readlines()
        is_before_food_name = True
        current_line = 0

        while current_line < len(lines):
            parsed_line = lines[current_line].replace('\n', '')
            if is_before_food_name:
                foods[parsed_line] = int(lines[current_line+1].replace('\n', ''))
                current_line += 1
            if parsed_line == '':
                is_before_food_name = True
            else:
                is_before_food_name = False
            current_line += 1

    result = []
    for food, time in foods.items():
        if time<=prep_time:
            result.append(f'{food}, preparation time {time} min')
    return result

def search_by_ingredient(filename: str, ingredient: str):
    # TODO

