# NH 2nd Caesar Cipher

def caesar_cipher(text, shift, mode='encrypt'):

    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decoding

    for char in text:
        # Check if the character is an alphabet letter and not a special char or number.
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

# Example Usage:
user_phrase = input("What's your phrase? ")
shift_value = int(input("And what's the shift value? "))

# Encoding the phrase
encoded_message = caesar_cipher(user_phrase, shift_value, mode='encrypt')
print(f"So your message was: {user_phrase}")
print(f"But I've encoded it and now it's: {encoded_message}")

# Decoding the message
decoded_message = caesar_cipher(encoded_message, shift_value, mode='decrypt')
print(f"And the decoded version is: {decoded_message}")