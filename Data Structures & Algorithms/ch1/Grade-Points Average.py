print("Welcome to the GPA Calculator.")
print("Enter your your letter grade one by line.")
print("Enter a blank line to designate the end.")
points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.67,
    'B+': 3.33,
    'B': 3.0,
    'B-': 2.67,
    'C+': 2.33,
    'C': 2.0,
    'C-': 1.67,
    'D+': 1.33,
    'D': 1.0,
    'F': 0.0
}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print(f"Unknown grade {grade}.")
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:
    print(f"Your Grade is {total_points/num_courses}")