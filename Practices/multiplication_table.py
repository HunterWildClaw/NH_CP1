# NH 2nd Mulitplication Table
import time
print("Welcome User! Here at Multi Table, we do all your multiplication for you. And here's a free demo table!")
time.sleep(3)

for x in range(1,13,1): print(f"{1*x}\t{2*x}\t{3*x}\t{4*x}\t{5*x}\t{6*x}\t{7*x}\t{8*x}\t{9*x}\t{10*x}\t{11*x}\t{12*x}\n")
time.sleep(5)
    
num_1 = int(input("Now, what multiplication problem troubles you? I can help.\nInsert the first number of your problem: "))
num_2 = int(input("Hmm ok. Now insert second number: "))
time.sleep(1)
print("Ok I think I got it. Gimme a sec.")
time.sleep(1)
answer = num_1*num_2
print(f"Ah ha! The answer to your question is {answer}!")