#Cheon Kim Kim Song

import tenseal as ts # type: ignore

def create_ckks_context():
    """Create and return a CKKS encryption context."""
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context.global_scale = 2**40
    context.generate_galois_keys()
    return context

def string_to_floats(text):
    """Convert a string to a list of floating-point ASCII values."""
    return [float(ord(char)) for char in text]

def floats_to_string(float_list):
    """Convert a list of floating-point ASCII values back to a string."""
    return "".join(chr(int(round(num))) for num in float_list)

def encrypt_message(context, text):
    """Encrypt a string message using CKKS and return the encrypted vector."""
    float_vector = string_to_floats(text)
    encrypted_vector = ts.ckks_vector(context, float_vector)
    return encrypted_vector

def decrypt_message(encrypted_vector):
    """Decrypt and return the plaintext string."""
    decrypted_floats = encrypted_vector.decrypt()
    return floats_to_string(decrypted_floats)

def main():
    # Create CKKS context
    context = create_ckks_context()
    encrypted_vector = None  # Variable to store the encrypted message
    
    while True:
        print("\n1. Encrypt Message")
        print("2. Show Encrypted Message")
        print("3. Perform Homomorphic Addition")
        print("4. Perform Homomorphic Multiplication")
        print("5. Decrypt Message")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            encrypted_vector = encrypt_message(context, message)
            print("\nMessage encrypted successfully!")

        elif choice == "2":
            if encrypted_vector:
                print("\nEncrypted Message:", encrypted_vector.serialize())  # Show encrypted data
            else:
                print("\nNo encrypted message found! Please encrypt a message first.")

        elif choice == "3":
            if encrypted_vector:
                encrypted_vector = encrypted_vector + encrypted_vector
                print("\nHomomorphic Addition performed successfully!")
            else:
                print("\nPlease encrypt a message first!")

        elif choice == "4":
            if encrypted_vector:
                encrypted_vector = encrypted_vector * 2
                print("\nHomomorphic Multiplication performed successfully!")
            else:
                print("\nPlease encrypt a message first!")

        elif choice == "5":
            if encrypted_vector:
                decrypted_text = decrypt_message(encrypted_vector)
                print("\nDecrypted Message:", decrypted_text)
            else:
                print("\nNo encrypted message found! Please encrypt first.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
