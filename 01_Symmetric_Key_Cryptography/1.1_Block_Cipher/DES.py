# Data Encryption Standards(DES).

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_des(plain_text, key):
    cipher = DES.new(key, DES.MODE_CBC)  # DES in CBC mode
    iv = cipher.iv  # Initialization vector
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), DES.block_size))
    return base64.b64encode(iv + encrypted_text).decode()  # Encode as Base64

def decrypt_des(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:DES.block_size]  # Extract IV
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[DES.block_size:]), DES.block_size)
    return decrypted_text.decode()

# User Input
key = input("Enter an 8-byte encryption key for DES: ").encode()  # Convert user input to bytes
if len(key) != 8:
    raise ValueError("DES requires an 8-byte key.")

message = input("Enter your message: ")  # Take input from user

# Encrypt and Decrypt
encrypted = encrypt_des(message, key)
decrypted = decrypt_des(encrypted, key)

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
