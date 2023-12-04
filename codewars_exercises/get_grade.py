def get_grade(first_grade, second_grade, third_grade):
    average_grade = (first_grade + second_grade + third_grade)/3
    if average_grade >= 90:
        return "A"
    if average_grade >= 80 and average_grade < 90:
        return "B"
    if average_grade >= 70 and average_grade < 80:
        return "C"
    if average_grade >= 60 and average_grade < 70:
        return "D"
    else:
        return "F"