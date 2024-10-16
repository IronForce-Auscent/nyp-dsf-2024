numlist = []
records = int(input("Enter number of records: "))
for _ in range(records):
    numlist.append(int(input("Enter a number: ")))

print(f"Max: {max(numlist)}\nMin: {min(numlist)}\nSum: {sum(numlist)}\nAverage: {sum(numlist)/len(numlist)}")   