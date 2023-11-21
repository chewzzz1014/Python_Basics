name = input('Whom should I sign this to: ')
file_name = input('Where shall I save it:')
with open(file_name, 'w') as rf:
    rf.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')

########################################################

with open('diary.txt', 'a') as rf:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    action = int(input('Function'))

    while action != 0:
        if action == 1:
            diary_entry = input('Diary entry:')
            rf.write(diary_entry + '\n')
            print('Diary saved')
        elif action == 2:
            with open('diary.txt') as rf1:
                for line in rf1:
                    print(line.replace('\n', ''))
        print('1 - add an entry, 2 - read entries, 0 - quit')
        action = int(input('Function'))
print('Bye now!')

########################################################

def write_to_file(file_name, content):
    with open(file_name, 'a') as rf:
        rf.write(content)
def filter_solutions():
    # clear files first
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()

    with open('solutions.csv') as rf:
        for line in rf:
            parsed_vals = line.replace('\n', '').split(';')
            expression = parsed_vals[1].split('+')
            operation = '+'
            if len(expression) < 2:
                expression = parsed_vals[1].split('-')
                operation = '-'
            print(expression)

            if operation == '+':
                if (int(expression[0]) + int(expression[1])) == int(parsed_vals[2]):
                    write_to_file('correct.csv', line)
                else:
                    write_to_file('incorrect.csv', line)
            elif operation == '+':
                if (int(expression[0]) - int(expression[1])) == int(parsed_vals[2]):
                    write_to_file('correct.csv', line)
                else:
                    write_to_file('incorrect.csv', line)

##############################################################

def store_personal_data(person: tuple):
    with open('people.csv', 'a') as rf:
        rf.write(f'{person[0]};{person[1]};{person[2]}\n')


##############################################################

import math

if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_data = input("Course information: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = 'exam_points1.csv'
    course_data = 'course1.txt'

students = {}
course = {}
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

with open(course_data) as rf:
    for line in rf:
        parsed_vals = line.replace('\n', '').split(': ')
        course[parsed_vals[0]] = parsed_vals[1]

cols = ['name', 'exec_nbr', 'exec_pts.', 'exm_pts.', 'tot_pts.', 'grade']
with open('results.txt', 'w') as rf:
    with open('results.csv', 'w') as rf1:
        rf.write(f'{course["name"]}, {course["study credits"]} credits\n')
        rf.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
        rf.write('======================================\n')

        for id, name in students.items():
            current_info = info[id]
            rf.write(
                f'{current_info[cols[0]]:22}{current_info[cols[1]]:10}{current_info[cols[2]]:10}{current_info[cols[3]]:10}{current_info[cols[4]]:10}{current_info[cols[5]]:10}\n')
            rf1.write(f'{id};{name};{current_info["grade"]}')

print('Results written to files results.txt and results.csv')
