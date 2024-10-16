numlist = []
for _ in range(10):
    numlist.append(int(input("Enter a number: ")))

print(f"Max: {max(numlist)}\nMin: {min(numlist)}\nSum: {sum(numlist)}\nAverage: {sum(numlist)/len(numlist)}")