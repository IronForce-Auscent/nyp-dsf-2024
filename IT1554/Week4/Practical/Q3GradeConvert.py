grade = input("Enter a grade: ").upper()

while grade not in ["A", "B", "C", "D"]:
    grade = input("Pleas enter a grade between A and D: ").upper()

if grade == "A":
    print("Your GPA is 4.0")
elif grade == "B": 
    print("Your GPA is 3.0")
elif grade == "C": 
    print("Your GPA is 2.0")
else:
    print("Your GPA is 1.0")


# oneliner solution
# print(f"Your GPA is {(lambda x: "4.0" if x == "A" else "3.0" if x == "B" else "2.0" if x == "C" else "1.0")(input("Enter a grade: ").upper())}")