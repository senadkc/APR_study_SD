print("deneme")
def check_grade(grade_tuple):
    midterm, final = grade_tuple
    average = (midterm + final) / 2

    if average >= 90:
        "Gectin"
    elif average >= 70:
        return "Notun"
    else:
        return "oldun"

student_grades = (75, 85)
result = check_grade(student_grades)
print(result)
print("deneme")