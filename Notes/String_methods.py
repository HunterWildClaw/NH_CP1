# NH 2nd String Methods notes

name = input("What's your name? ").strip().title()
# .lower() => makes it all lower case
#.upper() => all upper case
# .capitalize() => capitalize the first letter
# .title() => capitalizes the first letter of every word
age = int(input("Bro how old are you? "))

print("Hello {}, it is nice to meet you! I cant believe you are {:.2f}!".format(name, age))

print(f"Hello {name}, it is nice to meet you! I cant believe you are {age:.1f}!".format(name, age))

sentence = "The quick brown fox jumps over the lazy dog!"

word = "brown"
start = sentence.find(word)
length = len(word)


#print(sentence.replace(word, "yellow"))