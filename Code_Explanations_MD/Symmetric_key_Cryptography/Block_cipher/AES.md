# AES Code
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt_AES(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)  # AES Cipher in CBC mode
    iv = cipher.iv  # Initialization vector
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_text).decode()  # Encode as Base64

def decrypt_AES(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()

# Example Usage
key = get_random_bytes(16)  # 16 bytes key for AES-128
message = input("Enter your message: ")

encrypted = encrypt_AES(message, key)
decrypted = decrypt_AES(encrypted, key)

while True:
    print("\nChoose an option to display:")
    print("1. Encrypted Message")
    print("2. Decrypted Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print("Original Message:", message)
            print("Encrypted Message:", encrypted)
        case "2":
            print("Encrypted Message:", encrypted)
            print("Decrypted Message:", decrypted)
        case "3":
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")
```
## 1. Algorithmic Approach

This code uses AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode to encrypt and decrypt a plaintext message.

### Step 1: Key Generation
```python
key = get_random_bytes(16)
```
Generates a random 16-byte key for AES-128.
This key is used for both encryption and decryption.

### Step 2: Encryption
```python
def encrypt_AES(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_text).decode()
```
Create AES cipher in CBC mode:
CBC requires an Initialization Vector (IV) for the first block.
IV is randomly generated inside AES.new().

Pad plaintext:
AES works on blocks of 16 bytes.
If plaintext length is not multiple of block size, pad it using PKCS7.

Encrypt:
AES encrypts each block.
CBC uses previous ciphertext block XORed with current plaintext block.

Prepend IV:
First 16 bytes are IV, needed for decryption.

Base64 encode:
Converts bytes to a printable string.

### Step 3: Decryption
```python
def decrypt_AES(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()
```

Decode Base64:
Converts the string back to bytes.

Extract IV:
First 16 bytes are IV for CBC.

Decrypt ciphertext:
Use AES-CBC with the same key and IV.

Remove padding:
Recover the original plaintext bytes.

Decode to string:
Convert bytes back to UTF-8 text.

### Step 4: Interactive Display

Lets the user choose whether to display encrypted or decrypted messages.
Uses Python 3.10+ match-case for menu options.

## 2. Demo Input/Output

*User Input:*

Enter your message: Hello, AES Encryption!


*Example Run:*

Choose an option to display:
1. Encrypted Message
2. Decrypted Message
3. Exit


*Outputs:*

***Option 1: Encrypted Message***

Original Message: Hello, AES Encryption!
Encrypted Message: mOq7v8e2j6C9Q+1YBZ3yWJrFjE5f1B1ZVx8L8h4gXnU=


***Option 2: Decrypted Message***

Encrypted Message: mOq7v8e2j6C9Q+1YBZ3yWJrFjE5f1B1ZVx8L8h4gXnU=
Decrypted Message: Hello, AES Encryption!


***Option 3: Exit***

Exiting...


*Note: Encrypted message will differ each run because of the random IV.*

## 3. Time and Space Complexity Analysis
|Operation|	Time Complexity|	Space Complexity|	Explanation|
|:--------|:---------------|:-------------------|:-------------|
|AES Encryption (encrypt_AES)|	O(L)|	O(L)|	L = length of plaintext in bytes. Padding + block encryption is linear.|
|AES Decryption (decrypt_AES)|	O(L)|	O(L)|	Decrypt all blocks + unpad → linear in ciphertext size.|
|Base64 Encode/Decode|	O(L)|	O(L)|	Linear transformation of bytes to string and vice versa.|
|Overall Program|	O(L)|	O(L)|	Dominated by AES encryption/decryption over message length.|

*Notes:*

- AES block size = 16 bytes.

- CBC adds dependency on previous block, but still linear overall.

- Space complexity includes storing padded plaintext, ciphertext, and IV.

## 4. Summary

- Uses AES-128 in CBC mode for secure encryption.

- Random IV ensures different ciphertext for the same plaintext/key.

- Padding ensures plaintext fits AES block size.

- Base64 encoding is used for printable ciphertext.

- Time and space complexity scale linearly with message length.