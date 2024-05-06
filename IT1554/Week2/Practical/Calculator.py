"""scores = []
percentages = []

for i in range(1, 4):
    scores.append(float(input(f"What is your score for Test {i}: ")))
    percentages.append(float(input(f"What is percentage for Test {i}: ")))

scores.append(float(input("What is your score for Exam: ")))
percentages.append(50)
print("Your final mark is {0:.1f}".format(sum([x * (y/100) for x, y in zip(scores, percentages)])))"""

print("Your final mark is {0:.1f}".format((scores:=[], percentages:=[]), (scores.append(int(input(f"What is your score for Test {i // 2}"))) if i%2==1 else (percentages.append(int(input(f"What is percentage for Test {i // 2}")))) for i in range(2, 10)), (sum([x * (y/100) for x, y in zip(scores, percentages)]))))