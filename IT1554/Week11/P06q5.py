import re
sentence = "wheel of fortune"
p = re.compile('\w')
hidden_sentence = p.sub('-', sentence)
print('Guess the phrase :', hidden_sentence)
# while loop to keep asking for the letter and print out the phrase

while True:
    letter = input("Guess a letter: ")
    if letter in sentence:
        for i in range(len(sentence)):
            if sentence[i] == letter:
                hidden_sentence = hidden_sentence[:i] + letter + hidden_sentence[i+1:]
        print(f"Guess the phrase: {hidden_sentence}")
    
    if hidden_sentence == sentence:
        print("You have guessed the phrase!")
        break