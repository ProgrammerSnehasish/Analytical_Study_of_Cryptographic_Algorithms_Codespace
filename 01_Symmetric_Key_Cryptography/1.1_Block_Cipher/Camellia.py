#Camellia

import subprocess
import base64

def encrypt_camellia(plain_text, key):
    key_b64 = base64.b64encode(key).decode()
    plain_text_b64 = base64.b64encode(plain_text.encode()).decode()
    
    cmd = f"echo {plain_text_b64} | openssl enc -camellia-256-cbc -base64 -pass pass:{key_b64}"
    encrypted = subprocess.check_output(cmd, shell=True).decode().strip()
    
    return encrypted

def decrypt_camellia(encrypted_text, key):
    key_b64 = base64.b64encode(key).decode()
    
    cmd = f"echo {encrypted_text} | openssl enc -d -camellia-256-cbc -base64 -pass pass:{key_b64}"
    decrypted_b64 = subprocess.check_output(cmd, shell=True).decode().strip()
    decrypted_text = base64.b64decode(decrypted_b64).decode()
    
    return decrypted_text

# User Input
key = input("Enter encryption key (32 bytes for Camellia-256): ").encode()  # Convert user input to bytes
# Ensure the key is exactly 32 bytes
if len(key) < 32:
    key = key.ljust(32, b'\0')  # Pad with null bytes
elif len(key) > 32:
    key = key[:32]  # Truncate to 32 bytes

print(f"Final Key Length: {len(key)} bytes")  # Should always print 32

message = input("Enter your message: ")

# Encrypt and Decrypt
encrypted = encrypt_camellia(message, key)
decrypted = decrypt_camellia(encrypted, key)

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

#Note: This code uses OpenSSL's built-in Camellia (camellia-256-cbc)
#      Encrypts and decrypts using subprocess