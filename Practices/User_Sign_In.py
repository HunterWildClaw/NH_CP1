#NH 2nd user sign in

username = input("Give your username: ")
password = input("Give your password: ")

imported_username = input("Hello user. Please give username: ")
while imported_username != username:
    imported_username = input("Incorrect. Try again: ")
if imported_username == username:
    print("Success!")
else:
    print("Incorrect.")

imported_password = input("Hello user. Please give password: ")
while imported_password != password:
    imported_password = input("Incorrect. Try again: ")
if imported_password == password:
    print("Success!")
else:
    print("Incorrect.")


if imported_username == username and imported_password == password:
    print("Welcome HunterWildClaw! Login credentials were verified. You are welcome to get started.")
else:
    print("Login credentials could not be verified. Initiating self-destruct process.")