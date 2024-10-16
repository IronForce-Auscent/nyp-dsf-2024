student_answer = []
student_scores = []
correct_answer = ["C", "D", "B", "A", "B", "D", "A", "C", "D", "C"]

for _ in range(4):
    score = 0
    for _ in range(10):
        student_response = input("Enter your answer: ").upper()
        while student_response not in ["A", "B", "C", "D"]:
            student_response = input("Enter a valid answer: ").upper()

    for student_ans, correct_ans in zip(student_answer, correct_answer):
        if student_ans == correct_ans:
            score += 1
    student_scores.append(score)
    print(f"You have {score} correct answers and {len(correct_answer) - score} wrong answers.")
    retake = input("Do you want to retake the test? (Y/N): ").upper()
    while retake not in ["Y", "N"]:
        retake = input("Enter a valid response (Y/N): ").upper()
    if retake == "Y":
        student_answer.clear()
        continue
    else:
        print(f"Best attempt: {max(student_scores)}")
        print(f"Correct answers: {"".join(correct_answer)}")
        break