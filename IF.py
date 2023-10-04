def Grade(score):
    if score >=70 and score <=100:
        print("your score is", score, "and your grade is A")
    elif score >=60 and score <70:
        print("your score is", score, "and your grade is B")
    elif score>= 50 and score < 60:
        print("your score is", score, "and your grade is C")
    elif score >= 40 and score <50:
        print("your score is", score, "and your grade is D")
    else:
        print("your score is", score, " and You have FAILED!!")
Grade(76)
Grade(50)
Grade(30)
Grade(79)
Grade(65)

def Power(n,m):
    print("The power of", n, "to", m, "is", pow(n, m))
Power(3, 2)
Power(3, 5)
Power(5, 4)
