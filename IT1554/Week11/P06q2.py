to_strip = input("Enter a string: ")

lines_stripped = ""
for character in to_strip:
    if character.isspace():
        continue
    lines_stripped += character

print(lines_stripped)