total_gpa = 0
total_credit = 0

for i in range(5):
    credit = float(input(f"Enter the credit for subject {i + 1}: "))
    gpa = float(input(f"Enter the GPA for subject {i + 1}: "))
    total_gpa += gpa*credit
    total_credit += credit

cumgpa = total_gpa / total_credit
print(f"Your cumulative GPA for 5 modules is: {cumgpa}")