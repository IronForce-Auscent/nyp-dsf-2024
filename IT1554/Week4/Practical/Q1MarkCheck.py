marks = int(input("Enter marks for test: "))

if marks >= 50:
    print("You passed!")
else:
    print("You failed!")


# oneliner solution
# print("You passed" if int(input("Enter marks for test: ")) >= 50 else "You failed!") 

# Test data: 49, 50
# Expected output: You failed!, You passed!