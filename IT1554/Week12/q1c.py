numlist = []
records = int(input("Enter number of records: "))
for _ in range(records):
    numinput = int(input("Enter a number: "))
    while not numinput.is_integer():
        numinput = int(input("Enter a valid number: "))
    numlist.append(numinput)

print(f"Max: {max(numlist)}\nMin: {min(numlist)}\nSum: {sum(numlist)}\nAverage: {sum(numlist)/len(numlist)}")   