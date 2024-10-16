marks = {
    "Jane": {
        "English": 75,
        "Math": 80,
        "Science": 85
    }, 
    "John": {
        "English": 60,
        "Math": 68,
        "Science": 74
    },
    "Jerome": {
        "English": 81,
        "Math": 63,
        "Science": 77
    },
    "Jason": {
        "English": 55,
        "Math": 76,
        "Science": 67
    },
    "Jessica": {
        "English": 62,
        "Math": 45,
        "Science": 68
    },
    "Joanne": {
        "English": 52,
        "Math": 47,
        "Science": 51
    }
}

query = input("Enter name of student: ").capitalize()
if query in marks.keys():
    for key, value in marks[query].items():
        print(f"{key}: {value}")

elif query == "Average":
    for key, value in marks.items():
        print(f"Average marks of {key}: {round(sum(value.values())/len(value), 1)}")

elif query == "Subjects":
    subject_totals = {
        "English": 0,
        "Math": 0,
        "Science": 0
    }
    for _, value in marks.items():
        for subject, marks in value.items():
            subject_totals[subject] += marks
            
    for key, value in subject_totals.items():
        print(f"Average marks for {key}: {round(value / 6, 1)}")