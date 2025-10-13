#NH 2nd Password Strength Checker

#Make a variable called PASSWORD SCORE and add one to it evyertime it passes one of the tests.
password_score = 0
# Get password from user by asking them for it and make it a variable called PASSWORD.
password = input("What's your password? ")

# Check Password to make sure it at least had 8 chars in it. Then show how many characters it has in it. Do this by creating a line of code that has a new variable called PASSWORD LENGTH and define the variable as the length of the password. len(Password) will work. Then show how many characters it has in it so that you know.
password_length = str(len(password))
print("You password has " + password_length + " characters in it.")
password_length_num = int(len(password))
if password_length_num >= 8:
    password_score += 1
# checking password atributes
    # Check PASSWORD to make sure it has at least one uppercase letter in it. Then show the uppercase letters it has.
for upper_letter in password:
    if upper_letter in 'QWERTYUIOPASDFGHJKLZXCBNM':
        print("Your password has this capital letter in it: "+upper_letter+".")
        password_score += 1
    # Check PASSWORD to make sure it had at least one lowercase letter in it. Then show the lowercase letters it has.
for lower_letter in password:
    if lower_letter in 'qwertyuiopasdfghjklzxcvbnm':
        print("Your password has this lower case letter in it: "+lower_letter+".")
        password_score += 1
    # Check PASSWORD to make sure it has at least one number in it. Then show the numbers.
for number in password:
    if number in '1234567890':
        print("Your password has this number in it: "+number+".")
        password_score += 1
    # Check PASSWORD to make sure it has at least one special character in it. Then show the special chars it has.
for special_character in password:
    if special_character in '()!@#$%^&*()_+-=[]}{|;:",.<>?/':
        print("Your password has this special character in it: "+special_character+".")
        password_score += 1
    # If PASSWORD has at least 8 characters, one uppercase letter, one lower case letter, one number, and one special character in it, then show that it is a very strong password.
if password_score == 5:
    print("You have a very strong password.")
    # If one of those attributes are false, then say that it is a strong password.
elif password_score == 4:
    print("You have a strong password.")
    # If two of those attributes are false, then show that it's a moderate password. 
elif password_score == 3:
    print("Erm you have a moderate password. Make it better.")
    # If three or four of those attributes are false, then show that it's a weak password.
else:
    print("You have a weak password. Fix it now.")