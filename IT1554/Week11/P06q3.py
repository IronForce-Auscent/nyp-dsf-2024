user_input = input("Enter a string: ")

count = 0
for char in user_input:
    if char.isupper():
        count += 1

if count >= 2:
    print(user_input.upper())
else:
    print(user_input)