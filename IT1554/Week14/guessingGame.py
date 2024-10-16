import random

def generate_number():
    return random.randint(1,100)

def compare(guess, actual): 
    if guess > actual:
        result = "Too high"
    elif guess < actual:
        result = "Too low"
    else:
        result = "Bingo"
    return result

def main():
    actual = generate_number()
    score = 100
    guess = int(input("Enter a number between 1 to 100: "))
    result = compare(guess, actual)
    while result != "Bingo":
        score -= 1
        print(result)
        guess = int(input("Enter a number between 1 to 100: "))
        result = compare(guess, actual)
    print(f"{result}\nThe number is {actual} and your score is {score}")

if __name__ == "__main__":
    main()