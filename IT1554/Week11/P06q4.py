user_input = input("Enter a string: ")

if len(user_input) >= 5:
    if user_input[-3:] == "ing": 
        print(user_input + "ly")
    else:
        print(user_input + "ing")