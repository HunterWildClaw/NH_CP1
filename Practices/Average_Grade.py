# NH 2nd Average Grade

first_class = float(input("What is your grade for seminary?"))
second_class = float(input("What is your grade for CS 1400?"))
third_class =  float(input("What is your grade for biology?"))
fourth_class = float(input("What is your grade for advisory?"))
fifth_class = float(input("What is your grade for art?"))
sixth_class = float(input("What is your grade for english?"))
seventh_class = float(input("What is your grade for math? (I'm guessing it's not good. :)"))

average_grade = ((first_class + second_class + third_class + fourth_class + fifth_class + sixth_class + seventh_class)/7)
print(round(average_grade, 2),"Your GPA is", average_grade)