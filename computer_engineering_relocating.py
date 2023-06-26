GRADES = {
    "A": 4.00,
    "B": 3.00,
    "C": 2.00,
    "D": 1.00,
    "F": 0.00
}

students = []
for _ in range(2):
    student_number, gpx, computer_enginnering_grade, calculas_one_grade, calculas_two_grade = input().split()
    student = {
        "student_number": int(student_number),
        "gpx": float(gpx),
        "computer_enginnering_grade": computer_enginnering_grade.upper(),
        "calculas_one_grade": calculas_one_grade.upper(),
        "calculas_two_grade": calculas_two_grade.upper()
    }
    students.append(student)

passed_first_criterion = [
    student for student in students if
    student["computer_enginnering_grade"] == "A" and
    GRADES[student["calculas_one_grade"]] >= 2.00 and
    GRADES[student["calculas_two_grade"]] >= 2.00
]

if passed_first_criterion:
    passed_second_criterion = sorted(
        passed_first_criterion,
        key=lambda student: (
            student["gpx"],
            student["calculas_one_grade"],
            student["calculas_two_grade"]
        ), reverse=True
    )

    highest_student_grade = passed_second_criterion[0]

    if len(passed_second_criterion) > 1:
        lowest_student_grade = passed_second_criterion[1]

        same_conditionly: bool = False
        if highest_student_grade["gpx"] == lowest_student_grade["gpx"]:
            same_conditionly = True
        else:
            same_conditionly = False

        if highest_student_grade["calculas_one_grade"] == lowest_student_grade["calculas_one_grade"]:
            same_conditionly = True
        else:
            same_conditionly = False

        if highest_student_grade["calculas_two_grade"] == lowest_student_grade["calculas_two_grade"]:
            same_conditionly = True
        else:
            same_conditionly = False

        if same_conditionly:
            print("Both")
        else:
            print(None)
    else:
        print(highest_student_grade["student_number"])

else:
    print(None)
