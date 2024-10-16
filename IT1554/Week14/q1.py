def is_valid_nric(s: str):
    valid = False
    if len(s[1:-1]) == 7 and s[0].upper() in ["S", "T"] and s[-1].isalpha():
        valid = True
    return valid

# Test your function 3 times
print(is_valid_nric('t2323213t'))
print(is_valid_nric('s12323232'))
print(is_valid_nric('s'))


"""# Oneliner because fk you Wei Kiat
is_valid_nric = lambda s: len(s[1:-1]) == 7 and s[0].upper() in ["S", "T"] and s[-1].isalpha()
print(is_valid_nric('t2323213t'))
print(is_valid_nric('s12323232'))
print(is_valid_nric('s'))"""