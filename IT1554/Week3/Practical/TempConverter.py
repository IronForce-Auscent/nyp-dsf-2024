celsius = input("Enter temperature in Celsius: ")

while not celsius.isnumeric():
    celsius = input("Enter a valid temperature value: ")

fahrenheit = 9 / 5 * float(celsius) + 32
print(f"The temperature in Fahrenheit is {fahrenheit}")