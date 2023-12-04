def bmi(weight, height):
    bmi_calculation = weight/(height * height)
    if bmi_calculation <= 18.5:
        return "Underweight"
    if bmi_calculation <=25.0:
        return "Normal"
    if bmi_calculation <=30.0:
        return "Overweight"
    else:
        return "Obese"