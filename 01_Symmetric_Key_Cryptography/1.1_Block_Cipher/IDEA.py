#International Data Encryption Standards

import struct
import base64

# IDEA Constants
MODULO = 0x10001
MASK = 0xFFFF

class IDEA:
    def __init__(self, key):
        if len(key) != 16:
            raise ValueError("IDEA requires a 16-byte (128-bit) key.")
        self.subkeys = self.generate_subkeys(key)

    def generate_subkeys(self, key):
        key_words = list(struct.unpack(">8H", key))
        subkeys = key_words[:]

        for i in range(8, 52):
            if i % 8 == 0:
                subkeys.append(((subkeys[i - 7] << 9) | (subkeys[i - 6] >> 7)) & MASK)
            else:
                subkeys.append(((subkeys[i - 7] << 9) | (subkeys[i - 6] >> 7)) & MASK)
        return subkeys

    def mul(self, x, y):
        if x == 0:
            x = MODULO
        if y == 0:
            y = MODULO
        result = (x * y) % MODULO
        return result if result != MODULO else 0

    def inv(self, x):
        for i in range(1, MODULO):
            if (x * i) % MODULO == 1:
                return i
        return 0

    def generate_decryption_subkeys(self):
        decrypt_keys = [0] * 52
        decrypt_keys[48] = self.inv(self.subkeys[48])
        decrypt_keys[49] = -self.subkeys[49] & MASK
        decrypt_keys[50] = -self.subkeys[50] & MASK
        decrypt_keys[51] = self.inv(self.subkeys[51])

        for i in range(7, -1, -1):
            decrypt_keys[i * 6 + 4] = self.subkeys[i * 6 + 4]
            decrypt_keys[i * 6 + 5] = self.subkeys[i * 6 + 5]
            decrypt_keys[i * 6] = self.inv(self.subkeys[i * 6])
            decrypt_keys[i * 6 + 1] = -self.subkeys[i * 6 + 2] & MASK
            decrypt_keys[i * 6 + 2] = -self.subkeys[i * 6 + 1] & MASK
            decrypt_keys[i * 6 + 3] = self.inv(self.subkeys[i * 6 + 3])

        return decrypt_keys

    def encrypt_block(self, block, subkeys):
        x1, x2, x3, x4 = struct.unpack(">4H", block)

        for i in range(8):
            x1 = self.mul(x1, subkeys[i * 6])
            x2 = (x2 + subkeys[i * 6 + 1]) & MASK
            x3 = (x3 + subkeys[i * 6 + 2]) & MASK
            x4 = self.mul(x4, subkeys[i * 6 + 3])
            t1 = x1 ^ x3
            t2 = x2 ^ x4
            t1 = self.mul(t1, subkeys[i * 6 + 4])
            t2 = (t2 + t1) & MASK
            t2 = self.mul(t2, subkeys[i * 6 + 5])
            t1 = (t1 + t2) & MASK
            x1 ^= t2
            x4 ^= t1
            x2 ^= t1
            x3 ^= t2
            x2, x3 = x3, x2  # Swap x2 and x3

        x1 = self.mul(x1, subkeys[48])
        x2 = (x2 + subkeys[49]) & MASK
        x3 = (x3 + subkeys[50]) & MASK
        x4 = self.mul(x4, subkeys[51])

        return struct.pack(">4H", x1, x3, x2, x4)

    def encrypt(self, plaintext):
        padding_len = 8 - (len(plaintext) % 8)
        plaintext += chr(padding_len) * padding_len  # PKCS7 Padding
        return b"".join(self.encrypt_block(plaintext[i:i+8].encode(), self.subkeys) for i in range(0, len(plaintext), 8))

    def decrypt(self, ciphertext):
        subkeys = self.generate_decryption_subkeys()
        decrypted_bytes = b"".join(self.encrypt_block(ciphertext[i:i+8], subkeys) for i in range(0, len(ciphertext), 8))

        # Unpadding
        padding_len = decrypted_bytes[-1]
        return decrypted_bytes[:-padding_len].decode()

# User Input
key = input("Enter a 16-byte encryption key for IDEA: ").encode()
if len(key) != 16:
    raise ValueError("IDEA requires a 16-byte key.")

message = input("Enter your message: ")

# Encrypt and Decrypt
idea = IDEA(key)
encrypted = base64.b64encode(idea.encrypt(message)).decode()
decrypted = idea.decrypt(base64.b64decode(encrypted))

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
    menu_choice(choice)#User's Choice.


# import subprocess
# import base64
# import os

# def encrypt_idea(plain_text, key):
#     """Encrypts text using OpenSSL IDEA."""
#     key_b64 = base64.b64encode(key).decode()  # Encode key in Base64

#     # Write plaintext to a file
#     with open("plaintext.txt", "w") as f:
#         f.write(plain_text)

#     # Encrypt using OpenSSL IDEA-CBC
#     cmd = f"openssl enc -idea-cbc -base64 -pass pass:{key_b64} -in plaintext.txt -out encrypted.txt"
#     result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, text=True)

#     # Check if encryption was successful
#     if result.returncode != 0:
#         print("Encryption Error:", result.stderr.strip())  # Show error if encryption fails
#         return "Encryption failed."

#     # Read the encrypted content
#     with open("encrypted.txt", "r") as f:
#         encrypted_text = f.read().strip()
    
#     return encrypted_text

# def decrypt_idea(encrypted_text, key):
#     """Decrypts text using OpenSSL IDEA."""
#     key_b64 = base64.b64encode(key).decode()  # Encode key in Base64

#     # Write encrypted data to a file
#     with open("encrypted.txt", "w") as f:
#         f.write(encrypted_text)

#     # Decrypt using OpenSSL
#     cmd = f"openssl enc -d -idea-cbc -base64 -pass pass:{key_b64} -in encrypted.txt -out decrypted.txt"
#     result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, text=True)

#     # Check if decryption was successful
#     if result.returncode != 0:
#         print("Decryption Error:", result.stderr.strip())  # Show error if decryption fails
#         return "Decryption failed."

#     # Read the decrypted content
#     with open("decrypted.txt", "r") as f:
#         decrypted_text = f.read().strip()

#     return decrypted_text

# # User Input
# key = input("Enter a 16-byte encryption key for IDEA: ").encode()
# if len(key) != 16:
#     raise ValueError("IDEA requires a 16-byte key.")

# message = input("Enter your message: ")

# # Encrypt and Decrypt
# encrypted = encrypt_idea(message, key)
# decrypted = decrypt_idea(encrypted, key)

# # Function for switch-case behavior
# def menu_choice(choice):
#     options = {
#         "1": lambda: print(f"\nOriginal Message: {message}\nEncrypted Message: {encrypted}"),
#         "2": lambda: print(f"\nEncrypted Message: {encrypted}\nDecrypted Message: {decrypted}"),
#         "3": lambda: exit("\nExiting..."),
#     }
#     return options.get(choice, lambda: print("\nInvalid choice. Please try again."))()

# # Menu Loop
# while True:
#     print("\nChoose an option to display:")
#     print("1. Encrypted Message")
#     print("2. Decrypted Message")
#     print("3. Exit")

#     choice = input("Enter your choice: ")
#     menu_choice(choice)  # Call function based on user choice

# # Cleanup files
# os.remove("plaintext.txt") if os.path.exists("plaintext.txt") else None
# os.remove("encrypted.txt") if os.path.exists("encrypted.txt") else None
# os.remove("decrypted.txt") if os.path.exists("decrypted.txt") else None

#Note: This script encrypts and decrypts messages using OpenSSL's IDEA-CBC mode.