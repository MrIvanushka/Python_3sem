import math

student_levels = [int(i) for i in input().split()]
n = len(student_levels)
task_levels = [int(i) for i in input().split()]
k = len(task_levels)
good_students = 0

for student in student_levels:
    m = 0
    for task in task_levels:
        m += 1 / (1 + math.exp(-(student - task)/10))
    if m >= 0.5 * k:
        good_students += 1
print(good_students)
