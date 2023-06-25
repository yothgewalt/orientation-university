GRADES = {
    "A": 4.00,
    "B": 3.00,
    "C": 2.00,
    "D": 1.00,
    "F": 0.00
}

class Student:
    def __init__(
            self, student_number: int,
            gpx: float, computer_enginnering_grade: str,
            calculas_one_grade: str, calculas_two_grade: str
        ) -> None:
        self.student_number = student_number
        self.gpx = gpx
        self.computer_enginnering_grade = computer_enginnering_grade.upper()
        self.calculas_one_grade = calculas_one_grade.upper()
        self.calculas_two_grade = calculas_two_grade.upper()

students_data = []
for _ in range(2):
    student_number, gpx, computer_enginnering_grade, calculas_one_grade, calculas_two_grade = input().split()
    student = Student(int(student_number), float(gpx), computer_enginnering_grade, calculas_one_grade, calculas_two_grade)
    students_data.append(student)

passed_first_criterion = [
    student for student in students_data if
    student.computer_enginnering_grade == "A" and
    GRADES[student.calculas_one_grade] >= 2.00 and
    GRADES[student.calculas_two_grade] >= 2.00
]

if len(passed_first_criterion) > 1:
    passed_second_criterion = sorted(
        passed_first_criterion,
        key=lambda student: (
            student.gpx,
            student.calculas_one_grade,
            student.calculas_two_grade
        ), reverse=True
    )

    highest_student = passed_second_criterion[0]

    print(highest_student.student_number if highest_student else None)
elif len(passed_first_criterion) == 1:
    print(passed_first_criterion[0].student_number)
else:
    print(None)
