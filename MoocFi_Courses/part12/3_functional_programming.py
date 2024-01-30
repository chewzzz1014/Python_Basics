def names_of_students(attempts: list):
    return map(lambda a:a.student_name, attempts)

def course_names(attempts: list):
    return set(sorted(list(map(lambda a:a.course_name, attempts))))

class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts: list):
    return list(filter(lambda a:a.grade>=1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda a:a.grade==grade, attempts))

def passed_students(attempts: list, course: str):
    return sorted(list(set(map(lambda x:x.student_name,filter(lambda a:a.grade>0 and a.course_name==course, attempts)))))

from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda acc, x: acc+x.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda acc, x: acc+x.credits, list(filter(lambda a:a.grade>=1, attempts)), 0)

def average(attempts: list):
    filtered_attempts = list(filter(lambda a:a.grade>=1, attempts))
    return reduce(lambda acc, x: acc+x.grade, filtered_attempts, 0)/len(filtered_attempts)

