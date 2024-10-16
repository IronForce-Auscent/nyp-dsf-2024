weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in m): "))

bmi = weight / (height ** 2)
classification = ""
if bmi >= 27.5:
    classification = "Obese"
elif bmi >= 23 and bmi < 27.5:
    classification = "Overweight"
elif bmi >= 18.5 and bmi < 23:
    classification = "Normal"
else:
    classification = "Underweight"

print(f"Your BMI is {bmi:.2f} and you are {classification}")

# Oneline solution
# print("Your BMI is {:.2f} and you are {}".format((bmi:=float(input("Enter your weight (in kg): ")) / (float(input("Enter your height (in m): ")) ** 2)), ("obese" if bmi >= 27.5 else "overweight" if bmi >= 23 and bmi < 27.5 else "normal" if bmi >= 18 and bmi < 23 else "underweight")))