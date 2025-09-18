# NH 2nd Idiot Proof

name = input("What's your name? I promise I'm not a stalker. ")
phone_number = input("I swear I'm not stalking you... But what's your phone number? ")
gpa = input("Great! Now give me your gpa. ")

name = name.strip().title().replace("  "," ")
print(name)
phone_number = phone_number.replace("-"," ")

print(f"Hello {name}. I can now call you with the number {phone_number}. And you have a miserable {gpa:.2f} gpa. Oof.")