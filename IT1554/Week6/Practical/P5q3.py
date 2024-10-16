MARGINS = 1.25

cost_price = float(input("Enter cost price for item: "))
while cost_price > 0:
    print(f"Retail price is {cost_price * MARGINS}")