name = input("Enter name: ")
adminNo = input("Enter admin number: ")
age = int(input("Enter age: "))
gender = input("Enter gender (Male/Female): ")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

print(f"Hello! {name}\nYour admin no is {adminNo} and age is {age}\nYour gender is {gender} and bmi is {weight / height ** 2}")