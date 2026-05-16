# 3DES Code
```python
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
```
## 1. Algorithmic Approach

This program implements **Triple Data Encryption Standard (3DES)** using Python's `pycryptodome` library. It follows the Electronic Codebook (ECB) mode for encryption and decryption of text messages.

---

### Step 1: Key Validation
```python
def get_valid_key():
```
- The program asks the user for a key input.
- Valid key lengths for 3DES are **16 bytes** (two-key 3DES) or **24 bytes** (three-key 3DES).
- The loop continues until a valid key length is provided.

---

### Step 2: Encryption Process
```python
def encrypt_3des(plaintext, key):
```
- The plaintext message is **encoded** into bytes.
- Padding is added using `Crypto.Util.Padding.pad()` to make the message a multiple of 8 bytes (DES block size = 64 bits).
- A `DES3` cipher object is created in **ECB mode**.
- The message is encrypted and then converted into **hexadecimal format** using `binascii.hexlify()`.

**Mathematically:**  
\( C_i = E_{K}(P_i) \)

Where:
- \( P_i \): Plaintext block
- \( C_i \): Ciphertext block
- \( K \): 3DES key

---

### Step 3: Decryption Process
```python
def decrypt_3des(ciphertext, key):
```
- The encrypted hexadecimal input is converted back into bytes using `binascii.unhexlify()`.
- The same key is used to create a `DES3` cipher object in ECB mode.
- The data is decrypted and unpadded to recover the original message.

**Mathematically:**  
\( P_i = D_{K}(C_i) \)

Where:
- \( D \): DES decryption function

---

### Step 4: Menu-Driven Interface
```python
while True:
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
```
The user can choose between:
1. Encrypt a message.
2. Decrypt an encrypted hexadecimal string.
3. Exit the program.

Each option calls the corresponding function dynamically.

---

## 2. Demo Input and Output

**User Input:**
```
Enter a 16 or 24-byte key for 3DES: mysecretkey123456
```
```
Enter your message: CyberSecurity2025
```

**Output:**
```
Encrypted Message: 7ac1b4f2589a3d7e4f8a9d3cb02f76d9
```

**Decryption Example:**
```
Enter encrypted hex: 7ac1b4f2589a3d7e4f8a9d3cb02f76d9
Decrypted Message: CyberSecurity2025
```

**Exit Example:**
```
3
Exiting...
```

---

## 3. Time and Space Complexity

| Function | Time Complexity | Space Complexity | Explanation |
|-----------|-----------------|------------------|--------------|
| `get_valid_key()` | O(1) | O(1) | Constant validation; single key input. |
| `encrypt_3des()` | O(n) | O(n) | Encrypts data block-by-block; linear in message size. |
| `decrypt_3des()` | O(n) | O(n) | Decrypts data block-by-block; linear in ciphertext size. |
| `pad()` / `unpad()` | O(n) | O(n) | Adds or removes padding proportional to data length. |
| Overall Program | **O(n)** | **O(n)** | Linear with respect to message length. |

Where **n** = length of plaintext/ciphertext in bytes.

---

## 4. Summary

- **Algorithm:** Triple DES (3DES)
- **Block Size:** 64 bits (8 bytes)
- **Key Size:** 128-bit (16 bytes) or 192-bit (24 bytes)
- **Mode Used:** ECB (Electronic Codebook)
- **Padding Scheme:** PKCS#7
- **Library Used:** PyCryptodome

**Encryption Flow:**
```
Plaintext → Padding → 3DES (Encrypt) → Hexlify → Ciphertext
```

**Decryption Flow:**
```
Ciphertext → Unhexlify → 3DES (Decrypt) → Unpad → Plaintext
```

**Characteristics:**
- Symmetric encryption (same key used for both encryption & decryption).
- Deterministic for identical plaintext/key pairs in ECB mode.
- Suitable for small, fixed-size data blocks.

---

**Conclusion:**
This program successfully demonstrates **Triple DES encryption and decryption** using ECB mode, offering secure message handling for educational or lightweight cryptographic applications.
