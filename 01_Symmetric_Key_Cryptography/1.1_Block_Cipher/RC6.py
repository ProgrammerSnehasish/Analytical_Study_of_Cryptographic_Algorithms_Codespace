#Rivest Cipher 6 (RC6)

import struct
import base64

# RC6 Constants
W = 32  # Word size (32 bits)
R = 20  # Number of rounds
P32 = 0xB7E15163
Q32 = 0x9E3779B9

class RC6:
    def __init__(self, key):
        self.S = self.key_schedule(key)

    def key_schedule(self, key):
        """Generates round keys for RC6 encryption."""
        key = key.ljust(16, b'\x00')[:16]  # Ensure key is exactly 16 bytes
        L = list(struct.unpack('<4L', key))  # Convert key into 4 integers
        S = [(P32 + i * Q32) & 0xFFFFFFFF for i in range(2 * R + 4)]  # Generate key table

        A = B = i = j = 0
        for _ in range(3 * (2 * R + 4)):
            A = S[i] = self._rotate_left((S[i] + A + B) & 0xFFFFFFFF, 3)
            B = L[j] = self._rotate_left((L[j] + A + B) & 0xFFFFFFFF, (A + B) & 31)
            i = (i + 1) % (2 * R + 4)
            j = (j + 1) % 4
        return S

    def encrypt_block(self, block):
        """Encrypts a single 128-bit (16-byte) block."""
        A, B, C, D = struct.unpack('<4L', block)
        B = (B + self.S[0]) & 0xFFFFFFFF
        D = (D + self.S[1]) & 0xFFFFFFFF

        for i in range(1, R + 1):
            t = self._rotate_left((B * (2 * B + 1)) & 0xFFFFFFFF, 5)
            u = self._rotate_left((D * (2 * D + 1)) & 0xFFFFFFFF, 5)
            t &= 31  # Fix to ensure valid bit shift range
            u &= 31  # Fix to ensure valid bit shift range
            A = (self._rotate_left(A ^ t, u) + self.S[2 * i]) & 0xFFFFFFFF
            C = (self._rotate_left(C ^ u, t) + self.S[2 * i + 1]) & 0xFFFFFFFF
            A, B, C, D = B, C, D, A

        A = (A + self.S[2 * R + 2]) & 0xFFFFFFFF
        C = (C + self.S[2 * R + 3]) & 0xFFFFFFFF
        return struct.pack('<4L', A, B, C, D)

    def decrypt_block(self, block):
        """Decrypts a single 128-bit (16-byte) block."""
        A, B, C, D = struct.unpack('<4L', block)
        C = (C - self.S[2 * R + 3]) & 0xFFFFFFFF
        A = (A - self.S[2 * R + 2]) & 0xFFFFFFFF

        for i in range(R, 0, -1):
            A, B, C, D = D, A, B, C
            u = self._rotate_left((D * (2 * D + 1)) & 0xFFFFFFFF, 5)
            t = self._rotate_left((B * (2 * B + 1)) & 0xFFFFFFFF, 5)
            t &= 31  # Fix to ensure valid bit shift range
            u &= 31  # Fix to ensure valid bit shift range
            C = (self._rotate_right((C - self.S[2 * i + 1]) & 0xFFFFFFFF, t) ^ u)
            A = (self._rotate_right((A - self.S[2 * i]) & 0xFFFFFFFF, u) ^ t)

        D = (D - self.S[1]) & 0xFFFFFFFF
        B = (B - self.S[0]) & 0xFFFFFFFF
        return struct.pack('<4L', A, B, C, D)

    @staticmethod
    def _rotate_left(value, shift):
        """Performs a left bitwise rotation."""
        return ((value << shift) | (value >> (W - shift))) & 0xFFFFFFFF

    @staticmethod
    def _rotate_right(value, shift):
        """Performs a right bitwise rotation."""
        return ((value >> shift) | (value << (W - shift))) & 0xFFFFFFFF

# Helper Functions
def encrypt_rc6(plain_text, key):
    """Encrypts text using RC6."""
    cipher = RC6(key)
    padded_text = plain_text.ljust(16, ' ')[:16]  # Ensure 16-byte block
    encrypted_bytes = cipher.encrypt_block(padded_text.encode())
    return base64.b64encode(encrypted_bytes).decode()

def decrypt_rc6(encrypted_text, key):
    """Decrypts RC6 encrypted text."""
    cipher = RC6(key)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt_block(encrypted_bytes)
    return decrypted_bytes.decode().strip()

# User Input
key = input("Enter encryption key (16 bytes): ").encode()
if len(key) != 16:
    raise ValueError("Key length must be exactly 16 bytes.")

message = input("Enter your message: ")

# Encrypt and Decrypt
encrypted = encrypt_rc6(message, key)
decrypted = decrypt_rc6(encrypted, key)

# Menu Function
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
    menu_choice(choice)



# from rc6 import RC6Cipher
# from Crypto.Util.Padding import pad, unpad
# import base64

# BLOCK_SIZE = 16  # RC6 uses 128-bit (16-byte) blocks

# def encrypt_rc6(plain_text, key):
#     """Encrypts text using RC6 with CBC mode."""
#     cipher = RC6Cipher(key, mode="CBC")
#     iv = cipher.iv  # Initialization Vector
#     encrypted_text = cipher.encrypt(pad(plain_text.encode(), BLOCK_SIZE))
#     return base64.b64encode(iv + encrypted_text).decode()

# def decrypt_rc6(encrypted_text, key):
#     """Decrypts RC6 encrypted text."""
#     encrypted_text = base64.b64decode(encrypted_text)
#     iv = encrypted_text[:BLOCK_SIZE]  # Extract IV
#     cipher = RC6Cipher(key, mode="CBC", iv=iv)
#     decrypted_text = unpad(cipher.decrypt(encrypted_text[BLOCK_SIZE:]), BLOCK_SIZE)
#     return decrypted_text.decode()

# # User Input
# key = input("Enter encryption key (16, 24, or 32 bytes): ").encode()
# if len(key) not in (16, 24, 32):
#     raise ValueError("Key length must be 16, 24, or 32 bytes.")

# message = input("Enter your message: ")

# # Encrypt and Decrypt
# encrypted = encrypt_rc6(message, key)
# decrypted = decrypt_rc6(encrypted, key)

# # Menu Function
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
#     menu_choice(choice)
