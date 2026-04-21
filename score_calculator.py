def if_pass(score):
    return score >= 60
    
def cal_avg(score_value):
    return sum(score_value) / len(score_value)

def get_top_student(students):
    top_name = ""
    top_score = -99

    for student in students:
        if students[student] > top_score:
            top_score = student[student]
            top_name = student
    
    return top_name, top_score

scores = {}

while True:
    name = input("Please enter student name: ")
    if name == "q":
        break
    score = int(input("Please enter student's score: "))
    scores[name] = score

    if if_pass(score):
        print(f"{name}!! You PASS!!")
    else:
        print(f"{name}!! See you next year!!!")

average = cal_avg(scores.values())
print(f"Average is {average}")

highest_name, highest_score = get_top_student(scores)
print(f"{highest_name} got the highest score:{highest_score}")
