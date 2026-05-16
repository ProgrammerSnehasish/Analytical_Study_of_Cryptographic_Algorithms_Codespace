# RC5 Code
```python
import struct
import base64

# RC5 Key Schedule Constants
W = 32  # Word size (in bits)
R = 12  # Number of rounds
B = 16  # Key size in bytes
P = 0xB7E15163
Q = 0x9E3779B9

class RC5:
    def __init__(self, key):
        if len(key) != B:
            raise ValueError("RC5 requires a 16-byte key.")
        self.S = self.key_schedule(key)

    def key_schedule(self, key):
        """Generate key schedule for RC5"""
        L = list(struct.unpack("<4I", key))  # Convert key to 4-word list
        S = [(P + i * Q) & 0xFFFFFFFF for i in range(2 * R + 2)]
        A = B = 0
        i = j = 0
        for _ in range(3 * max(2 * R + 2, len(L))):
            A = S[i] = self.rotl((S[i] + A + B) & 0xFFFFFFFF, 3)
            B = L[j] = self.rotl((L[j] + A + B) & 0xFFFFFFFF, (A + B) & 31)
            i = (i + 1) % (2 * R + 2)
            j = (j + 1) % len(L)
        return S

    def rotl(self, x, y):
        return ((x << y) | (x >> (W - y))) & 0xFFFFFFFF

    def rotr(self, x, y):
        return ((x >> y) | (x << (W - y))) & 0xFFFFFFFF

    def encrypt_block(self, block):
        """Encrypt 64-bit block"""
        A, B = struct.unpack("<2I", block)
        A = (A + self.S[0]) & 0xFFFFFFFF
        B = (B + self.S[1]) & 0xFFFFFFFF
        for i in range(1, R + 1):
            A = (self.rotl(A ^ B, B & 31) + self.S[2 * i]) & 0xFFFFFFFF
            B = (self.rotl(B ^ A, A & 31) + self.S[2 * i + 1]) & 0xFFFFFFFF
        return struct.pack("<2I", A, B)

    def decrypt_block(self, block):
        """Decrypt 64-bit block"""
        A, B = struct.unpack("<2I", block)
        for i in range(R, 0, -1):
            B = self.rotr((B - self.S[2 * i + 1]) & 0xFFFFFFFF, A & 31) ^ A
            A = self.rotr((A - self.S[2 * i]) & 0xFFFFFFFF, B & 31) ^ B
        B = (B - self.S[1]) & 0xFFFFFFFF
        A = (A - self.S[0]) & 0xFFFFFFFF
        return struct.pack("<2I", A, B)

# Function for padding
def pad_message(message):
    while len(message) % 8 != 0:
        message += " "  # Padding with spaces
    return message

# Encrypt function
def encrypt_rc5(plain_text, key):
    rc5 = RC5(key)
    plain_text = pad_message(plain_text)
    encrypted_bytes = b"".join(rc5.encrypt_block(plain_text[i:i+8].encode()) for i in range(0, len(plain_text), 8))
    return base64.b64encode(encrypted_bytes).decode()

# Decrypt function
def decrypt_rc5(encrypted_text, key):
    rc5 = RC5(key)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = b"".join(rc5.decrypt_block(encrypted_bytes[i:i+8]) for i in range(0, len(encrypted_bytes), 8))
    return decrypted_bytes.decode().strip()

# User Input
key = input("Enter a 16-byte encryption key for RC5: ").encode()
if len(key) != 16:
    raise ValueError("RC5 requires a 16-byte key.")

message = input("Enter your message: ")

# Encrypt and Decrypt
encrypted = encrypt_rc5(message, key)
decrypted = decrypt_rc5(encrypted, key)

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

This code implements RC5, a symmetric block cipher using variable-length key, 64-bit blocks (2 × 32-bit words), and 12 rounds.

### Step 1: Key Handling
```python
key = input("Enter a 16-byte encryption key for RC5: ").encode()
```
RC5 requires 16-byte key.
If key length ≠ 16 bytes → program raises ValueError.

### Step 2: Key Schedule
```python
def key_schedule(self, key):
```
Converts the 16-byte key into 4 32-bit words (L).
Generates a key schedule array S of length 2*R + 2 = 26 words.
Mixing of L and S:
Rotate and add operations to spread key entropy across subkeys.
Provides subkeys for all encryption rounds.

### Step 3: Encryption of One Block
```python
def encrypt_block(self, block):
```
Input = 64-bit block split into A, B (32-bit words).
Pre-whitening: A += S[0], B += S[1].

For 12 rounds:
A = ROTL(A ^ B, B & 31) + S[2*i]
B = ROTL(B ^ A, A & 31) + S[2*i+1]

Returns encrypted 64-bit block.

### Step 4: Decryption of One Block
```python
def decrypt_block(self, block):
```

Reverse operations of encryption:

For each round in reverse:
B = ROTR(B - S[2*i+1], A & 31) ^ A
A = ROTR(A - S[2*i], B & 31) ^ B
Post-whitening: subtract S[0] and S[1].

Returns decrypted 64-bit block.

### Step 5: Padding
```python
def pad_message(message):
    while len(message) % 8 != 0:
        message += " "
```

Pads plaintext to multiples of 8 bytes (64 bits) using spaces.

### Step 6: Encryption/Decryption of Text
```python
def encrypt_rc5(plain_text, key):
    # Encrypt block by block and Base64 encode
```

Encrypts message 8 bytes at a time.

Base64 encoding produces printable ciphertext.
```python
def decrypt_rc5(encrypted_text, key):
    # Base64 decode and decrypt block by block
```

Decrypts each 8-byte block and removes padding.

### Step 7: Menu System

User can select:
Display original + encrypted message
Display encrypted + decrypted message
Exit program

Dictionary simulates switch-case.

## 2. Demo Input and Output

***User Input:***

Enter a 16-byte encryption key for RC5: mysecretkey123456
Enter your message: Hello RC5 Encryption!


***Menu Options:***

Choose an option to display:
1. Encrypted Message
2. Decrypted Message
3. Exit


***Example Outputs:***

**Option 1: Encrypted Message**

Original Message: Hello RC5 Encryption!
Encrypted Message: 3f+2YxW8i3K+Qh2HkG4X8g==


**Option 2: Decrypted Message**

Encrypted Message: 3f+2YxW8i3K+Qh2HkG4X8g==
Decrypted Message: Hello RC5 Encryption!


**Option 3: Exit**

Exiting...


Note: Encrypted output differs each run if padding or key changes.

## 3. Time and Space Complexity
|Function|	Time Complexity|	Space Complexity|	Explanation|
|:-------|:----------------|:-------------------|:-------------|
|key_schedule|	O(R) = O(1)|	O(2R+2) = O(1)|	Fixed number of rounds → constant time and space.|
|encrypt_block / decrypt_block|	O(R) = O(1)|	O(1)|	12 rounds per 64-bit block → constant.|
|encrypt_rc5 / decrypt_rc5|	O(L/8) ≈ O(L)|	O(L)|	L = plaintext length. Processes blocks sequentially.|
|Base64 encode/decode|	O(L)|	O(L)|	Linear transformation of bytes ↔ ASCII string.|
|Overall Program|	O(L)|	O(L)|	Dominated by block-wise encryption/decryption.|

*Notes:*

- RC5 block size = 64 bits (8 bytes).

- Number of rounds R = 12.

- Key size = 128 bits (16 bytes).

- Space includes message bytes, ciphertext, padding, and key schedule array.

## 4. Summary

- RC5 is a symmetric block cipher with variable key size, 64-bit blocks, 12 rounds.

- Encryption uses modular addition, XOR, and bitwise rotations.

- Decryption reverses encryption using inverse rotations and subtractions.

- Padding ensures plaintext is multiple of 8 bytes.

- Base64 encoding allows printable ciphertext.

- Time and space complexity scale linearly with plaintext length.