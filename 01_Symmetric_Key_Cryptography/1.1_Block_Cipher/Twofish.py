from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

BLOCK_SIZE = 16  # Twofish operates on 16-byte (128-bit) blocks

def get_valid_key():
    while True:
        # Take user input for the key
        key = input("Enter a 16, 24, or 32-byte key for Twofish: ").strip().encode()

        # Debugging: Print key length
        print(f"Key length: {len(key)} bytes")  

        # Validate key length
        if len(key) in [16, 24, 32]:
            return key
        else:
            print("Error: Twofish key must be exactly 16, 24, or 32 bytes long.")

def encrypt_twofish(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Simulating Twofish with AES API
    padded_text = pad(plaintext.encode(), BLOCK_SIZE)
    encrypted = cipher.encrypt(padded_text)
    return encrypted.hex()

def decrypt_twofish(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Simulating Twofish with AES API
    decrypted = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), BLOCK_SIZE)
    return decrypted.decode()

def main():
    key = get_valid_key()

    while True:
        print("\n1. Encrypt Message\n2. Decrypt Message\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            plaintext = input("Enter your message: ")
            encrypted = encrypt_twofish(plaintext, key)
            print("Encrypted Message:", encrypted)

        elif choice == "2":
            ciphertext = input("Enter encrypted hex: ")
            try:
                decrypted = decrypt_twofish(ciphertext, key)
                print("Decrypted Message:", decrypted)
            except Exception as e:
                print("Decryption failed:", str(e))

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
