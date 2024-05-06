timeinsecs = int(input("Enter time in seconds: "))
hours = timeinsecs // 3600
minutes = (timeinsecs % 3600) // 60
seconds = (timeinsecs % 60) % 60
print(f"{timeinsecs} seconds is {hours} hours, {minutes} minutes and {seconds} seconds")