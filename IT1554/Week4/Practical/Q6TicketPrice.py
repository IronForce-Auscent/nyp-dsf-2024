age = int(input("Enter your age: "))

while not (age >= 4 and age <= 130): 
    age = int(input("Please enter an age between 4 and 130: "))

day = int(input("Enter the day of visit: "))


price = 0
if day in (6, 7):
    price = 10
else:
    if age < 16: 
        price = 7.5
    elif age >= 16 and age < 65:
        price = 10
    else:
        price = 5.5

print(f"You have to pay ${price:.2f} for your ticket")

# oneliner solution
# print(f"You have to pay ${((lambda x, y: 10 if y in (6, 7) else 7.5 if x < 16 else 10 if x >= 16 and x < 65 else 5.5)(int(input("Enter your age: ")), int(input("Enter your day of visit: ")))):.2f}")


# Test data: (15, 6), (15, 7), (15, 1), (16, 1), (65, 1), (64, 1)
# Expected output: 10.00, 10.00, 7.50, 10.00, 5.50, 10.00