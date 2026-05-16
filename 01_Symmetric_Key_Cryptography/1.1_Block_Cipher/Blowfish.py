#Blowfish

from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_blowfish(plain_text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)  # Blowfish in CBC mode
    iv = cipher.iv  # Initialization vector
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), Blowfish.block_size))
    return base64.b64encode(iv + encrypted_text).decode()  # Encode as Base64

def decrypt_blowfish(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:Blowfish.block_size]  # Extract IV
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[Blowfish.block_size:]), Blowfish.block_size)
    return decrypted_text.decode()

# User Input
key = input("Enter encryption key (4 to 56 bytes): ").encode()  # Convert user input to bytes
if not (4 <= len(key) <= 56):
    raise ValueError("Key length must be between 4 and 56 bytes.")

message = input("Enter your message: ")  # Take input from user

# Encrypt and Decrypt
encrypted = encrypt_blowfish(message, key)
decrypted = decrypt_blowfish(encrypted, key)

# Function for switch-case behavior
def menu_choice(choice):
    options = {
        "1": lambda: print(f"\nOriginal Message: {message}\nEncrypted Message: {encrypted}"),
        "2": lambda: print(f"\nEncrypted Message: {encrypted}\nDecrypted Message: {decrypted}"),
        "3": lambda: exit("\nExiting..."),
    }
    return options.get(choice, lambda: print("\nInvalid choice. Please try again."))()

# Menu Loop
while True:
    print("\nChoose an option to display:")
    print("1. Encrypted Message")
    print("2. Decrypted Message")
    print("3. Exit")

    choice = input("Enter your choice: ")
    menu_choice(choice)  # Call function based on user choice
