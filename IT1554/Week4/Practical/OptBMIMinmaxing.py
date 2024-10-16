"""RECOMMENDED_MAX = 22.9
RECOMMENDED_MIN = 18.5

height = input("Enter your height (in m): ")

while not height.replace(".", "").isnumeric():
    height = input("Invalid input! Please try again. ")

height = float(height)

weight_lim1 = RECOMMENDED_MIN * (height ** 2)
weight_lim2 = RECOMMENDED_MAX * (height ** 2)
print(f"Your weight should be between {weight_lim1:.2f}kg and {weight_lim2:.2f}kg to be considered healthy")"""


# oneliner solution

RECOMMENDED_MAX = 22.9
RECOMMENDED_MIN = 18.5

def test():
    height = input("Enter your height (in m): ")
    try:
        height = float(height)
        weight_lim1 = RECOMMENDED_MIN * (height ** 2)
        weight_lim2 = RECOMMENDED_MAX * (height ** 2)
        print(f"Your weight should be between {weight_lim1:.2f}kg and {weight_lim2:.2f}kg to be considered healthy")
    except ValueError as e:
        print("Invalid input! Try again")
        test()
    except Exception as e2:
        raise e2


test()