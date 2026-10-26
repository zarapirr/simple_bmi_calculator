weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

if weight <= 0 or height <= 0:
    print("Error: Weight and height must be positive numbers.")
else:
    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obesity")
