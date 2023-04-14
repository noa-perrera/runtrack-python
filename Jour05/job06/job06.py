def round_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            next_multiple_of_5 = (grade // 5 + 1) * 5
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades

grades = [73, 72, 38, 33]
rounded_grades = round_grades(grades)
print(rounded_grades)