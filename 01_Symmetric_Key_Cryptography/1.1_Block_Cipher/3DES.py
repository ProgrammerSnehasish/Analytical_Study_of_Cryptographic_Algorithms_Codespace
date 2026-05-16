from Crypto.Cipher import DES3 # type: ignore
from Crypto.Util.Padding import pad, unpad # type: ignore
import binascii

def get_valid_key():
    """Ensure the user provides a valid 16 or 24-byte key."""
    while True:
        key = input("Enter a 16 or 24-byte key for 3DES: ").encode()
        if len(key) in (16, 24):
            return key
        print("Error: 3DES key must be exactly 16 or 24 bytes long.")

def encrypt_3des(plaintext, key):
    """Encrypt message using 3DES."""
    cipher = DES3.new(key, DES3.MODE_ECB)  # Using ECB mode
    padded_text = pad(plaintext.encode(), DES3.block_size)
    encrypted = cipher.encrypt(padded_text)
    return binascii.hexlify(encrypted).decode()

def decrypt_3des(ciphertext, key):
    """Decrypt message using 3DES."""
    cipher = DES3.new(key, DES3.MODE_ECB)  # Using ECB mode
    decrypted_padded = cipher.decrypt(binascii.unhexlify(ciphertext))
    return unpad(decrypted_padded, DES3.block_size).decode()

def main():
    """Main function to run the encryption/decryption program."""
    key = get_valid_key()
    
    while True:
        print("\n1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter your message: ")
            encrypted = encrypt_3des(message, key)
            print(f"Encrypted Message: {encrypted}")

        elif choice == "2":
            encrypted_hex = input("Enter encrypted hex: ")
            try:
                decrypted = decrypt_3des(encrypted_hex, key)
                print(f"Decrypted Message: {decrypted}")
            except Exception as e:
                print(f"Error in decryption: {e}")

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
