# Write your solution here
import math

def get_inputs():
    exam_point_arr = []
    exercise_completed_arr = []

    user_input = input('Exam points and exercises completed:')
    while user_input != '':
        exam_point = int(user_input.split(' ')[0])
        exercise_completed = int(user_input.split(' ')[1])
        exam_point_arr.append(exam_point)
        exercise_completed_arr.append(exercise_completed)
        user_input = input('Exam points and exercises completed:')
    return [exam_point_arr, exercise_completed_arr]

def calc_exercise_point(arr):
    result = []
    for i in arr:
        result.append(math.floor(i/10))
    return result

def cal_avg_points(exam_points, exercise_points):
    sum = 0
    for i in range(len(exam_points)):
        sum += exam_points[i] + exercise_points[i]
    return sum/len(exercise_points)

def get_grade(exam_points, exercise_points):
    total = exam_points + exercise_points
    grade = 5
    if exam_points<10:
        grade = 0
    elif 0<=total<=14:
        grade = 0
    elif 15<=total<=17:
        grade = 1
    elif 18<=total<=20:
        grade = 2
    elif 21<=total<=23:
        grade = 3
    elif 24<=total<=27:
        grade = 4
    elif 28<=total<=30:
        grade = 5
    return grade


# start main
input_results = get_inputs()

print('Statistics:')
exam_point_arr = input_results[0]
exercise_completed_arr = input_results[1]
exercise_point_arr = calc_exercise_point(exercise_completed_arr)

# point avg
avg_points = cal_avg_points(exam_point_arr, exercise_point_arr)
print(f'Points average: {avg_points:.1f}')

# pass percentage and grade dist
num_passed = 0
grades = [0,0,0,0,0,0]
for i in range(len(exam_point_arr)):
    grade = get_grade(exam_point_arr[i], exercise_point_arr[i])
    grades[grade] += 1
    if grade != 0:
        num_passed += 1
print(f'Pass percentage:{(num_passed/len(exam_point_arr)*100): .1f}')
print('Grade distribution:')
for i in range(5,-1,-1):
        print(f'  {i}: {"*"*grades[i]}')

