import urllib.request as ur
import json
import math

def print_persons(filename: str):
    with open(filename) as rf:
        data = rf.read()
        person = json.loads(data)
        for p in person:
           print(f'{p["name"]} {p["age"]} year ({", ".join(p["hobbies"])})')

print_persons('file1.json')

###############################################################
def retrieve_all():
    results = []
    res = ur.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses')
    data = json.loads(res.read())
    for course in data:
        results.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
    print(results)

def retrieve_course(course_name: str):
    results = {}
    try:
        res = ur.urlopen(f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats')
        data = json.loads(res.read())

        num_weeks = 0
        num_students = 0
        sum_hours = 0
        avg_hour = 0
        sum_exercises = 0
        avg_exercises = 0
        # print(data)
        # for w in data:
        for week, week_data in data.items():
            num_week += 1
            num_students += week_data['students']
            sum_hours += week_data['hour_total']
            sum_exercises += week_data['exercise_total']

        results = {
            'weeks': num_week,
            'students': num_students,
            'hours': sum_hours,
            'hours_average': round(sum_hours/num_students),
            'exercises': sum_exercises,
            'exercises_average': round(sum_exercises/num_students)
        }
        return results
    except:
        return results

print(retrieve_course("docker2019"))

###############################################################