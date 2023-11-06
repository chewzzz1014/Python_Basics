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


# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []


def print_student(students: dict, name: str):
    if name not in students:
        print(f'{name}: no such person in the database')
        return
    if len(students[name]) == 0:
        print(f'{name}:')
        print(' no completed courses')
    else:
        courses = students[name]
        print(f'{name}:')
        print(f' {len(courses)} completed courses:')
        for course in courses:
            print(f'  {course[0]} {course[1]}')
        avg_grade = calc_avg_grade(courses)
        print(f' average grade {avg_grade:.1f}')


def calc_avg_grade(courses: list):
    sum = 0
    for course in courses:
        sum += course[1]
    return sum / len(courses)


def add_course(students: dict, name: str, course: tuple):
    if course[1] > 0:
        has_added = False
        for i in range(len(students[name])):
            existing_course = students[name][i]
            if (existing_course[0] == course[0]):
                has_added = True
                if existing_course[1] < course[1]:
                    students[name][i] = course
                    break
        if not has_added:
            students[name].append(course)


def summary(students: dict):
    total_student = 0
    max_courses_completed = 0
    max_courses_completed_student = ''
    best_avg_grade = 0
    best_avg_grade_student = ''
    for name in students:
        total_student += 1
        courses = students[name]

        courses_completed = len(courses)
        if courses_completed > max_courses_completed:
            max_courses_completed = courses_completed
            max_courses_completed_student = name

        avg_grade = calc_avg_grade(courses)
        if avg_grade > best_avg_grade:
            best_avg_grade = avg_grade
            best_avg_grade_student = name
    print(f'students {total_student}')
    print(f'most courses completed {max_courses_completed} {max_courses_completed_student}')
    print(f'best average grade {best_avg_grade:.1f} {best_avg_grade_student}')

