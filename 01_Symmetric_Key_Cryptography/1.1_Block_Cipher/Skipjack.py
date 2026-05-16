#Skipjack 

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def encrypt_aes(plaintext, key):
    # Generate a random IV
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def decrypt_aes(ciphertext, key):
    # Decode the base64 encoded string
    data = base64.b64decode(ciphertext)
    iv = data[:16]  # Extract the IV
    ciphertext = data[16:]  # Extract the actual ciphertext
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted.decode('utf-8')

def main():
    key = os.urandom(16)  # AES requires a 16-byte key for AES-128
    print(f"Key (base64): {base64.b64encode(key).decode('utf-8')}")

    while True:
        print("\n1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter your message: ")
            encrypted = encrypt_aes(message, key)
            print("Encrypted Message (base64):", encrypted)

        elif choice == "2":
            encrypted_message = input("Enter encrypted message (base64): ")
            decrypted = decrypt_aes(encrypted_message, key)
            print("Decrypted Message:", decrypted)

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
