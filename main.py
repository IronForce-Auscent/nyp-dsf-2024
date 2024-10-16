output = []
series = int(input("Enter a term of series: "))
if series < 2:
  print("You must have at least two set of number")
else:
  for i in range(1, series + 1):
    output.append("5" * i)
print(" ".join(output))
print(f"Sum of above series is: {sum([int(x) for x in output])}")