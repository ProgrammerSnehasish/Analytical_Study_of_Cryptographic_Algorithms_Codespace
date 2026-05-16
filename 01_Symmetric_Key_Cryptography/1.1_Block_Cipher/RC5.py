# Rivest Cipher 5 (RC5)

import struct
import base64

# RC5 Key Schedule Constants
W = 32  # Word size (in bits)
R = 12  # Number of rounds
B = 16  # Key size in bytes
P = 0xB7E15163
Q = 0x9E3779B9

class RC5:
    def __init__(self, key):
        if len(key) != B:
            raise ValueError("RC5 requires a 16-byte key.")
        self.S = self.key_schedule(key)

    def key_schedule(self, key):
        """Generate key schedule for RC5"""
        L = list(struct.unpack("<4I", key))  # Convert key to 4-word list
        S = [(P + i * Q) & 0xFFFFFFFF for i in range(2 * R + 2)]
        A = B = 0
        i = j = 0
        for _ in range(3 * max(2 * R + 2, len(L))):
            A = S[i] = self.rotl((S[i] + A + B) & 0xFFFFFFFF, 3)
            B = L[j] = self.rotl((L[j] + A + B) & 0xFFFFFFFF, (A + B) & 31)
            i = (i + 1) % (2 * R + 2)
            j = (j + 1) % len(L)
        return S

    def rotl(self, x, y):
        return ((x << y) | (x >> (W - y))) & 0xFFFFFFFF

    def rotr(self, x, y):
        return ((x >> y) | (x << (W - y))) & 0xFFFFFFFF

    def encrypt_block(self, block):
        """Encrypt 64-bit block"""
        A, B = struct.unpack("<2I", block)
        A = (A + self.S[0]) & 0xFFFFFFFF
        B = (B + self.S[1]) & 0xFFFFFFFF
        for i in range(1, R + 1):
            A = (self.rotl(A ^ B, B & 31) + self.S[2 * i]) & 0xFFFFFFFF
            B = (self.rotl(B ^ A, A & 31) + self.S[2 * i + 1]) & 0xFFFFFFFF
        return struct.pack("<2I", A, B)

    def decrypt_block(self, block):
        """Decrypt 64-bit block"""
        A, B = struct.unpack("<2I", block)
        for i in range(R, 0, -1):
            B = self.rotr((B - self.S[2 * i + 1]) & 0xFFFFFFFF, A & 31) ^ A
            A = self.rotr((A - self.S[2 * i]) & 0xFFFFFFFF, B & 31) ^ B
        B = (B - self.S[1]) & 0xFFFFFFFF
        A = (A - self.S[0]) & 0xFFFFFFFF
        return struct.pack("<2I", A, B)

# Function for padding
def pad_message(message):
    while len(message) % 8 != 0:
        message += " "  # Padding with spaces
    return message

# Encrypt function
def encrypt_rc5(plain_text, key):
    rc5 = RC5(key)
    plain_text = pad_message(plain_text)
    encrypted_bytes = b"".join(rc5.encrypt_block(plain_text[i:i+8].encode()) for i in range(0, len(plain_text), 8))
    return base64.b64encode(encrypted_bytes).decode()

# Decrypt function
def decrypt_rc5(encrypted_text, key):
    rc5 = RC5(key)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = b"".join(rc5.decrypt_block(encrypted_bytes[i:i+8]) for i in range(0, len(encrypted_bytes), 8))
    return decrypted_bytes.decode().strip()

# User Input
key = input("Enter a 16-byte encryption key for RC5: ").encode()
if len(key) != 16:
    raise ValueError("RC5 requires a 16-byte key.")

message = input("Enter your message: ")

# Encrypt and Decrypt
encrypted = encrypt_rc5(message, key)
decrypted = decrypt_rc5(encrypted, key)

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
