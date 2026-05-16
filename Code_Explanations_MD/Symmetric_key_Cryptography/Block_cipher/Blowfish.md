# Blowfish Code
```python
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_blowfish(plain_text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)  # Blowfish in CBC mode
    iv = cipher.iv  # Initialization vector
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), Blowfish.block_size))
    return base64.b64encode(iv + encrypted_text).decode()  # Encode as Base64

def decrypt_blowfish(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:Blowfish.block_size]  # Extract IV
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[Blowfish.block_size:]), Blowfish.block_size)
    return decrypted_text.decode()

# User Input
key = input("Enter encryption key (4 to 56 bytes): ").encode()  # Convert user input to bytes
if not (4 <= len(key) <= 56):
    raise ValueError("Key length must be between 4 and 56 bytes.")

message = input("Enter your message: ")  # Take input from user

# Encrypt and Decrypt
encrypted = encrypt_blowfish(message, key)
decrypted = decrypt_blowfish(encrypted, key)

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
```
## 1. Algorithmic Approach

This code implements Blowfish encryption in CBC (Cipher Block Chaining) mode.

### Step 1: Key Input
```python
key = input("Enter encryption key (4 to 56 bytes): ").encode()
```
Blowfish supports keys of length 4 to 56 bytes.
User-provided key is converted to bytes.
If key is invalid, program raises a ValueError.

### Step 2: Encryption
```python
def encrypt_blowfish(plain_text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    iv = cipher.iv
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), Blowfish.block_size))
    return base64.b64encode(iv + encrypted_text).decode()
```

Initialize Blowfish in CBC mode:
CBC mode requires an Initialization Vector (IV).
Randomly generated IV ensures different ciphertexts for the same plaintext/key.

Pad plaintext:
Blowfish block size = 8 bytes.
PKCS7 padding ensures plaintext length is multiple of block size.

Encrypt:
CBC encrypts each block using XOR with the previous ciphertext block.

Prepend IV:
First 8 bytes = IV for decryption.

Base64 encode:
Converts ciphertext to printable string.

### Step 3: Decryption
```python
def decrypt_blowfish(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:Blowfish.block_size]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[Blowfish.block_size:]), Blowfish.block_size)
    return decrypted_text.decode()
```

Decode Base64 → converts string to bytes.
Extract IV → first 8 bytes.
Decrypt using Blowfish-CBC.
Unpad decrypted bytes → recover original plaintext.
Convert bytes to string.

### Step 4: Menu System
```python
while True:
    choice = input("Enter your choice: ")
    menu_choice(choice)
```

Allows the user to select:
Display encrypted message
Display decrypted message
Exit

Uses a dictionary to simulate switch-case behavior in Python.

## 2. Demo Input and Output

*User Input:*

Enter encryption key (4 to 56 bytes): mysecretkey
Enter your message: Hello, Blowfish CBC!


*Menu Options:*

Choose an option to display:
1. Encrypted Message
2. Decrypted Message
3. Exit


*Example Outputs:*

***Option 1: Encrypted Message***

Original Message: Hello, Blowfish CBC!
Encrypted Message: h3c2f8+5Tzq4VJzZy+Q6a8zQF1eE4t+X6vClz8Qy8yM=


***Option 2: Decrypted Message***

Encrypted Message: h3c2f8+5Tzq4VJzZy+Q6a8zQF1eE4t+X6vClz8Qy8yM=
Decrypted Message: Hello, Blowfish CBC!


***Option 3: Exit***

Exiting...


Note: Encrypted message differs each run because the IV is random.

## 3. Time and Space Complexity
|Function|	Time Complexity|	Space Complexity|	Explanation|
|:-------|:----------------|:-------------------|:-------------|
|encrypt_blowfish|	O(L)|	O(L)|	L = length of plaintext. Padding + block encryption = linear time. CBC adds linear dependency.|
|decrypt_blowfish|	O(L)|	O(L)|	Linear decryption + unpadding.|
|Base64 encode/decode|	O(L)|	O(L)|	Linear transformation of bytes to string.|
|Overall Program|	O(L)|	O(L)|	Dominated by encryption/decryption of message length.|

*Notes:*
- Blowfish block size = 8 bytes.
- CBC mode requires XOR with previous ciphertext → still linear overall.

## 4. Summary

- Blowfish-CBC encryption securely encrypts data with a variable-length key.

- IV ensures unique ciphertexts for repeated plaintexts.

- PKCS7 padding ensures block alignment.

- Time and space complexity scale linearly with message length.

- Menu allows interactive viewing of encrypted/decrypted messages.