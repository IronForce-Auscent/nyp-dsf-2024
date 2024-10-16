int_sum = 0
num = int(input("Enter number: "))

while num != 0:
    int_sum += num
    num = int(input("Enter another number: "))

print(f"The sum of the numbers is {int_sum}")