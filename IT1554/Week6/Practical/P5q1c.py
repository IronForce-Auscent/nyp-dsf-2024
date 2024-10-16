sum = 0
num = int(input("Enter number: "))
while num < 2:
    num = int(input("Enter a number greater than or equal to 2: "))

for i in range(1, num + 1):
    if i % 2 == 0:
        sum += i
    
print(f"The sum is {sum}")