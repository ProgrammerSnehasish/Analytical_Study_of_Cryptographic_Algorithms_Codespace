# Advance Encryption Standards(AES).

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt_AES(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)  # AES Cipher in CBC mode
    iv = cipher.iv  # Initialization vector
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_text).decode()  # Encode as Base64

def decrypt_AES(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()

# Example Usage
key = get_random_bytes(16)  # 16 bytes key for AES-128
message = input("Enter your message: ")

encrypted = encrypt_AES(message, key)
decrypted = decrypt_AES(encrypted, key)

while True:
    print("\nChoose an option to display:")
    print("1. Encrypted Message")
    print("2. Decrypted Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print("Original Message:", message)
            print("Encrypted Message:", encrypted)
        case "2":
            print("Encrypted Message:", encrypted)
            print("Decrypted Message:", decrypted)
        case "3":
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")