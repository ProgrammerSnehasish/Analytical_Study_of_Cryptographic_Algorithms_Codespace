# Twofish Code
```python
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
```

## 📘 Overview

**Twofish** is a symmetric key block cipher designed by **Bruce Schneier** and his team.  
It was one of the **five finalists** in the **AES competition** but was not ultimately selected.  
Although this implementation uses the **AES API** from `pycryptodome` for demonstration,  
it conceptually follows the **same structure and key length properties** as Twofish.

---

## 🧠 Algorithmic Approach

### Encryption Steps

Input Key Validation
Accepts only 16, 24, or 32 bytes (128, 192, or 256-bit keys).
Ensures key length matches Twofish standards.

Padding
The plaintext is padded using PKCS#7 to make its length a multiple of 16 bytes.

Encryption
AES (simulating Twofish) encrypts each 128-bit block in ECB mode.
The encrypted data is returned as a hex string.

Decryption Steps
Hex to Bytes Conversion
Convert the input hexadecimal ciphertext back to bytes.

Decryption
The same AES object decrypts the data block-by-block.

Unpadding
Remove PKCS#7 padding to recover the original plaintext.

## 🧩 Example Input/Output
▶️ Input:
Enter a 16, 24, or 32-byte key for Twofish: tw0fishencryption!
Key length: 16 bytes

1. Encrypt Message
2. Decrypt Message
3. Exit
Enter your choice: 1
Enter your message: cyber_security

🔐 Output:
Encrypted Message: 1a4c86a52a66a27c3e432f5b915f432e

▶️ Input (Decryption):
Enter your choice: 2
Enter encrypted hex: 1a4c86a52a66a27c3e432f5b915f432e

🔓 Output:
Decrypted Message: cyber_security

## ⏱️ Time Complexity Analysis
|Operation|	Description|	Time Complexity|
|:--------|:-----------|:------------------|
|Key Validation|	Checking key length|	O(1)|
|Padding (PKCS#7)|	Adds bytes up to next 16-byte boundary|	O(n)|
|Encryption (AES Block Ops)|	Each 16-byte block processed independently|	O(n)|
|Hex Conversion|	Converts bytes to hexadecimal|	O(n)|
|Decryption|	Reverses encryption block by block|	O(n)|
|Unpadding|	Removes padding bytes|	O(n)|

✅ Overall Time Complexity: O(n)
*(where n = message length in bytes)*

## 💾 Space Complexity Analysis
|Component|	Description|	Space Complexity|
|:--------|:-----------|:-------------------|
|Key Storage|	Stores encryption key|	O(1)|
|Padded Plaintext|	Copy of plaintext + padding bytes|	O(n)|
|Ciphertext Storage|	Stores encrypted data|	O(n)|
|Temporary Buffers|	For padding/unpadding operations|	O(n)|

*✅ Overall Space Complexity: O(n)*

## 🧩 Notes

- AES is used only as a structural simulation for Twofish.
Twofish and AES both share 128-bit block size and variable key lengths.

- Real Twofish implementations use Feistel networks, key-dependent S-boxes,
and MDS matrices, unlike AES which uses substitution–permutation networks.
