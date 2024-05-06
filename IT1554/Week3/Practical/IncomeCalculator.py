yearly = float(input("Enter yearly gross salary: "))
monthly = yearly / 12
take_home = monthly * 0.8 - 1500
print(f"Monthly take-home pay is ${take_home:.2f}")