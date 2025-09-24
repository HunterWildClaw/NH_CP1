#NH 2nd What is my grade?

grade = float(input("What is your grade? "))

if grade > 95:
    print(f"Congrats! You have an A! That's {grade}%")
elif grade <= 95 and grade > 90:
    print(f"You have and A-. So close! It's at {grade}%")
elif grade <= 90 and grade > 85:
    print(f"You're at a B+. That's {grade}%")
elif grade <= 85 and grade > 80:
    print(f"You've got a B. Keep at it! That's {grade}%")
elif grade <= 80 and grade > 75:
    print(f"You have a B-. Try to keep that B. That's {grade}%")
elif grade <= 75 and grade > 70:
    print(f"Yeesh. You've got a C+. Start working harder. That's {grade}%")
elif grade <= 70 and grade > 65:
    print(f"You have a C. Ouch. That's {grade}%")
elif grade <= 65 and grade > 60:
    print(f"You have a C-. That's horrible! That's {grade}%")
elif grade <= 60 and grade > 55:
    print(f"You have a D+. Don't quit your day job. That's {grade}%")
elif grade <= 55 and grade > 50:
    print(f"You have a D. Get some help. That's {grade}%")
elif grade <= 50 and grade > 45:
    print(f"You have a D-. Oof. That's {grade}%")
elif grade <= 45 and grade >= 0:
    print(f"You have an F. I suggest you work you butt off and try harder. That's {grade}%")
else:
    print(f"That's not a grade. Try again.")