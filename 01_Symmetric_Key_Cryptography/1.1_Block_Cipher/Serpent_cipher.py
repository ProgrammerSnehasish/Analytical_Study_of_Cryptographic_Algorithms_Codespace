#Serpent

# S-boxes for the Serpent cipher
S_BOXES = [
    [
        0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x6,
        0x2, 0x0, 0x5, 0xC, 0x3, 0xE, 0xF, 0x7,
        0xD, 0x0, 0xB, 0x7, 0x4, 0xE, 0x1, 0xA,
        0x2, 0xC, 0x3, 0x8, 0xF, 0x5, 0x6, 0x9,
        0xE, 0x1, 0x0, 0xB, 0xC, 0x4, 0xA, 0x3,
        0x7, 0xD, 0x5, 0x2, 0x8, 0x6, 0x9, 0xF,
        0x3, 0x8, 0xD, 0x1, 0x2, 0x4, 0x7, 0x6,
        0x5, 0xA, 0x0, 0xC, 0xE, 0x9, 0xB, 0xF
    ],
    # Additional S-boxes would be defined here...
] * 8  # Repeat the same S-box for demonstration purposes

INVERSE_S_BOXES = [
    [
        0x9, 0x6, 0x4, 0xC, 0x1, 0xE, 0x2, 0xB,
        0xF, 0x8, 0x3, 0x7, 0xA, 0x0, 0x5, 0xD,
        0x3, 0xA, 0x0, 0x4, 0xC, 0x9, 0x1, 0xF,
        0x7, 0x8, 0xE, 0xD, 0x6, 0x2, 0xB, 0x5,
        0xE, 0x7, 0xB, 0x2, 0x3, 0xC, 0xA, 0x6,
        0xF, 0x9, 0x5, 0x0, 0xD, 0x8, 0x1, 0x4,
        0xC, 0x5, 0xA, 0xB, 0x9, 0x1, 0x3, 0xE,
        0x7, 0xF, 0x0, 0x6, 0x8, 0xD, 0x2, 0x4
    ],
    # Additional inverse S-boxes would be defined here...
] * 8  # Repeat the same inverse S-box for demonstration

# Number of rounds
NUM_ROUNDS = 32

def s_box_lookup(value, s_box):
    """Look up the value in the S-box."""
    return s_box[value]

def key_schedule(key):
    """Generate round keys from the original key."""
    # This is a simplified key schedule for demonstration purposes.
    return [key[i % len(key)] for i in range(NUM_ROUNDS)]

def serpent_encrypt(plaintext, key):
    """Encrypt the plaintext using the Serpent cipher."""
    round_keys = key_schedule(key)
    state = list(plaintext)

    for round_num in range(NUM_ROUNDS):
        # Apply S-boxes (correcting the 8-bit to 4-bit issue)
        new_state = []
        for byte in state:
            high_nibble = (byte >> 4) & 0xF  # Upper 4 bits
            low_nibble = byte & 0xF          # Lower 4 bits

            new_high = s_box_lookup(high_nibble, S_BOXES[round_num % len(S_BOXES)])
            new_low = s_box_lookup(low_nibble, S_BOXES[round_num % len(S_BOXES)])

            new_state.append((new_high << 4) | new_low)  # Combine back to 8-bit

        state = new_state  # Update state after S-box transformation

        # XOR with round key
        state = [state[i] ^ round_keys[round_num] for i in range(len(state))]

    return bytes(state)

def serpent_decrypt(ciphertext, key):
    """Decrypt the ciphertext using the Serpent cipher."""
    round_keys = key_schedule(key)
    state = list(ciphertext)

    for round_num in range(NUM_ROUNDS - 1, -1, -1):
        # XOR with round key
        state = [state[i] ^ round_keys[round_num] for i in range(len(state))]

        # Apply inverse S-boxes (fixing incorrect S-box usage)
        new_state = []
        for byte in state:
            high_nibble = (byte >> 4) & 0xF  # Upper 4 bits
            low_nibble = byte & 0xF          # Lower 4 bits

            new_high = s_box_lookup(high_nibble, INVERSE_S_BOXES[round_num % len(INVERSE_S_BOXES)])
            new_low = s_box_lookup(low_nibble, INVERSE_S_BOXES[round_num % len(INVERSE_S_BOXES)])

            new_state.append((new_high << 4) | new_low)  # Combine back to 8-bit

        state = new_state  # Update state after S-box transformation

    return bytes(state)

def main():
    last_encrypted = None  # To store the last encrypted message

    while True:
        print("\n1. Encrypt Message")
        print("2. Decrypt Last Encrypted Message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key_input = input("Enter your key (32 hex digits): ")
            if len(key_input) != 32:  # 32 hex digits = 16 bytes
                print("Key must be 32 hex digits (16 bytes).")
                continue
            
            # Convert hex input to bytes
            key = bytes.fromhex(key_input)

            plaintext_input = input("Enter your plaintext (32 hex digits): ")
            if len(plaintext_input) != 32:  # 32 hex digits = 16 bytes
                print("Plaintext must be 32 hex digits (16 bytes).")
                continue
            
            # Convert hex input to bytes
            plaintext = bytes.fromhex(plaintext_input)

            # Encrypt the plaintext
            encrypted = serpent_encrypt(plaintext, key)
            last_encrypted = encrypted  # Store the last encrypted message
            print("Encrypted (hex):", encrypted.hex())

        elif choice == "2":
            if last_encrypted is None:
                print("No encrypted message to decrypt.")
                continue
            
            key_input = input("Enter your key (32 hex digits): ")
            if len(key_input) != 32:
                print("Key must be 32 hex digits (16 bytes).")
                continue
            
            key = bytes.fromhex(key_input)

            # Decrypt the last encrypted message
            decrypted = serpent_decrypt(last_encrypted, key)
            print("Decrypted (hex):", decrypted.hex())

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

#TODO: fix output.

# import base64
# from serpent import encrypt, decrypt

# def main():
#     last_encrypted = None  # To store the last encrypted message

#     while True:
#         print("\n1. Encrypt Message")
#         print("2. Decrypt Last Encrypted Message")
#         print("3. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             key_input = input("Enter your key (16 hex digits): ")
#             if len(key_input) != 32:  # 16 hex digits = 8 bytes
#                 print("Key must be 32 hex digits (16 bytes).")
#                 continue
            
#             # Convert hex input to bytes
#             key = bytes.fromhex(key_input)

#             plaintext_input = input("Enter your plaintext (16 hex digits): ")
#             if len(plaintext_input) != 32:  # 16 hex digits = 8 bytes
#                 print("Plaintext must be 32 hex digits (16 bytes).")
#                 continue
            
#             # Convert hex input to bytes
#             plaintext = bytes.fromhex(plaintext_input)

#             # Encrypt the plaintext
#             encrypted = encrypt(key, plaintext)
#             last_encrypted = encrypted  # Store the last encrypted message
#             print("Encrypted (base64):", base64.b64encode(encrypted).decode())

#         elif choice == "2":
#             if last_encrypted is None:
#                 print("No message has been encrypted yet.")
#             else:
#                 # Decrypt the last encrypted message
#                 decrypted = decrypt(key, last_encrypted)
#                 print("Decrypted (hex):", decrypted.hex())

#         elif choice == "3":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()


# from Crypto.Cipher import Serpent
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes
# import base64

# # Function to encrypt using Serpent
# def encrypt_serpent(plain_text, key):
#     cipher = Serpent.new(key, Serpent.MODE_CBC)
#     iv = cipher.iv  # Get the Initialization Vector (IV)
#     ciphertext = cipher.encrypt(pad(plain_text.encode(), 16))  # Encrypt and pad the text
#     return base64.b64encode(iv + ciphertext).decode()  # Encode result in Base64

# # Function to decrypt using Serpent
# def decrypt_serpent(encrypted_text, key):
#     raw_data = base64.b64decode(encrypted_text)  # Decode Base64 data
#     iv, ciphertext = raw_data[:16], raw_data[16:]  # Extract IV and ciphertext
#     cipher = Serpent.new(key, Serpent.MODE_CBC, iv)
#     return unpad(cipher.decrypt(ciphertext), 16).decode()

# # User Input
# key = input("Enter a 32-byte encryption key: ").encode()
# if len(key) != 32:
#     raise ValueError("Key must be exactly 32 bytes (256-bit).")

# message = input("Enter your message: ")

# # Encrypt & Decrypt
# encrypted = encrypt_serpent(message, key)
# decrypted = decrypt_serpent(encrypted, key)

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