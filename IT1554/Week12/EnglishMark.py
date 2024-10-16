marks = {
    "Jane": 75, 
    "John": 60,
    "Jerome": 81
}

for key, value in marks.items():
    print(f"{key}: {value}")

query = input("Enter name of student: ").capitalize()
if query in marks.keys():
    print(f"Results for English: {marks[query]}")