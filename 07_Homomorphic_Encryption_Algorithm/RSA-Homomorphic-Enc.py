#RSA Homomorphic Encryption

from Crypto.PublicKey import RSA # type: ignore
from Crypto.Util.number import bytes_to_long, long_to_bytes # type: ignore

def generate_keys():
    """Generate RSA key pair."""
    key = RSA.generate(2048)
    public_key = key.publickey()
    return key, public_key

def encrypt(message, public_key):
    """Encrypt a message (string or number) using RSA public key."""
    if message.isdigit():
        message_int = int(message)
    else:
        message_int = bytes_to_long(message.encode())  # Convert string to integer
    
    ciphertext = pow(message_int, public_key.e, public_key.n)
    return ciphertext

def decrypt(ciphertext, private_key):
    """Decrypt ciphertext using RSA private key and return original string or number."""
    plaintext_int = pow(ciphertext, private_key.d, private_key.n)  # RSA Decryption: m = c^d mod n
    
    try:
        return long_to_bytes(plaintext_int).decode()  # Convert integer back to string
    except UnicodeDecodeError:
        return plaintext_int  # Return numeric value if conversion fails

def homomorphic_multiplication(ciphertext, multiplier, public_key):
    """Perform homomorphic multiplication: Enc(m) * multiplier = Enc(m^multiplier mod n)."""
    return pow(ciphertext, multiplier, public_key.n)

def main():
    # Generate RSA Key Pair
    private_key, public_key = generate_keys()
    encrypted_message = None

    while True:
        print("\n1. Encrypt Message")
        print("2. Perform Homomorphic Multiplication")
        print("3. Decrypt Message")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter a message (text or number): ")
            encrypted_message = encrypt(message, public_key)
            print("Encrypted Message:", encrypted_message)

        elif choice == "2":
            if encrypted_message is None:
                print("Error: No message has been encrypted yet!")
                continue
            multiplier = int(input("Enter a number to multiply with: "))
            encrypted_message = homomorphic_multiplication(encrypted_message, multiplier, public_key)
            print("Encrypted Result:", encrypted_message)

        elif choice == "3":
            if encrypted_message is None:
                print("Error: No message has been encrypted yet!")
                continue
            decrypted_message = decrypt(encrypted_message, private_key)
            print("Decrypted Message:", decrypted_message)

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

#Note: After multiplication (except multiply by 1) the code doesn't return the original plain text, instade of that it returns a long number.