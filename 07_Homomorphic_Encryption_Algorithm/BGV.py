#BGV

import numpy as np # type: ignore

# Simple mock BGV encryption function (real BGV is complex)
def bgv_encrypt(numbers, key):
    encrypted = [(num + key) % 256 for num in numbers]  # Simple modular shift
    return encrypted

# Simple mock BGV decryption function
def bgv_decrypt(encrypted_numbers, key):
    decrypted = [(num - key) % 256 for num in encrypted_numbers]
    return decrypted

# Convert text to ASCII values
def text_to_ascii(text):
    return [ord(char) for char in text]

# Convert ASCII values back to text
def ascii_to_text(ascii_values):
    return ''.join(chr(num) for num in ascii_values)

def main():
    key = int(input("Enter a numeric key for encryption (integer only): "))

    while True:
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter your message: ")
            ascii_values = text_to_ascii(message)
            encrypted = bgv_encrypt(ascii_values, key)
            print("Encrypted Message (ASCII Values):", encrypted)

        elif choice == "2":
            encrypted_input = input("Enter encrypted numbers (comma-separated): ")
            encrypted_numbers = list(map(int, encrypted_input.split(',')))
            decrypted_ascii = bgv_decrypt(encrypted_numbers, key)
            decrypted_text = ascii_to_text(decrypted_ascii)
            print("Decrypted Message:", decrypted_text)

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
