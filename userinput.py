score = int(input("please enter the student's score:"))
name = str(input("please enter your name:"))
if score >= 70 and score <=100:
    print("your name is", name, "your score is", score, "and your grade is A")
elif score >= 60 and score <70:
    print("your name is", name, "your score is", score, "and your grade is B")
elif score >= 50 and score < 60:
    print("your name is", name, "your score is", score, "and your grade is C")
elif score >= 40 and score < 50:
    print("your name is", name, "your score is", score, "and your grade is D")
else:
    print("your name is", name, "your score is", score, " and You have FAILED!!")
