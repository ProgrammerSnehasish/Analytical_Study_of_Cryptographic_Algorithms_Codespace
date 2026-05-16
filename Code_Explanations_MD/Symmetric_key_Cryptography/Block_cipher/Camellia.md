# Camellia Code
```python
import subprocess
import base64

def encrypt_camellia(plain_text, key):
    key_b64 = base64.b64encode(key).decode()
    plain_text_b64 = base64.b64encode(plain_text.encode()).decode()
    
    cmd = f"echo {plain_text_b64} | openssl enc -camellia-256-cbc -base64 -pass pass:{key_b64}"
    encrypted = subprocess.check_output(cmd, shell=True).decode().strip()
    
    return encrypted

def decrypt_camellia(encrypted_text, key):
    key_b64 = base64.b64encode(key).decode()
    
    cmd = f"echo {encrypted_text} | openssl enc -d -camellia-256-cbc -base64 -pass pass:{key_b64}"
    decrypted_b64 = subprocess.check_output(cmd, shell=True).decode().strip()
    decrypted_text = base64.b64decode(decrypted_b64).decode()
    
    return decrypted_text

# User Input
key = input("Enter encryption key (32 bytes for Camellia-256): ").encode()  # Convert user input to bytes
# Ensure the key is exactly 32 bytes
if len(key) < 32:
    key = key.ljust(32, b'\0')  # Pad with null bytes
elif len(key) > 32:
    key = key[:32]  # Truncate to 32 bytes

print(f"Final Key Length: {len(key)} bytes")  # Should always print 32

message = input("Enter your message: ")

# Encrypt and Decrypt
encrypted = encrypt_camellia(message, key)
decrypted = decrypt_camellia(encrypted, key)

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

#Note: This code uses OpenSSL's built-in Camellia (camellia-256-cbc)
#      Encrypts and decrypts using subprocess
```
## 1. Algorithmic Approach

This code uses OpenSSL via subprocess to encrypt and decrypt text using Camellia-256 in CBC mode.

### Step 1: Key Handling
```python
key = input("Enter encryption key (32 bytes for Camellia-256): ").encode()
```
Camellia-256 requires a 32-byte key.
If the input key is less than 32 bytes, it’s padded with null bytes (\0).
If more than 32 bytes, it’s truncated.
Key is then Base64 encoded for passing to OpenSSL:
```python
key_b64 = base64.b64encode(key).decode()
```
### Step 2: Encryption
```python
def encrypt_camellia(plain_text, key):
    plain_text_b64 = base64.b64encode(plain_text.encode()).decode()
    cmd = f"echo {plain_text_b64} | openssl enc -camellia-256-cbc -base64 -pass pass:{key_b64}"
    encrypted = subprocess.check_output(cmd, shell=True).decode().strip()
    return encrypted
```
Base64 encode plaintext → ensures safe ASCII input to OpenSSL.
Run OpenSSL command:
enc -camellia-256-cbc → encrypt with Camellia-256 in CBC mode.
-base64 → output Base64 ciphertext.
-pass pass:{key} → supply password/key.
Read output → encrypted Base64 string.

### Step 3: Decryption
```python
def decrypt_camellia(encrypted_text, key):
    cmd = f"echo {encrypted_text} | openssl enc -d -camellia-256-cbc -base64 -pass pass:{key_b64}"
    decrypted_b64 = subprocess.check_output(cmd, shell=True).decode().strip()
    decrypted_text = base64.b64decode(decrypted_b64).decode()
    return decrypted_text
```
Run OpenSSL decrypt command with same key.
Base64 decode output → recover original plaintext bytes.
Decode bytes → convert to string.

### Step 4: Menu System
Uses a dictionary to simulate switch-case behavior.
Options:
Display encrypted message
Display decrypted message
Exit

## 2. Demo Input and Output

*User Input:*

Enter encryption key (32 bytes for Camellia-256): mysecurekey1234567890abcdef
Enter your message: Hello Camellia Encryption!


*Example Run:*

***Option 1: Encrypted Message***

Original Message: Hello Camellia Encryption!
Encrypted Message: U2FsdGVkX1+Hg/3q1e4YpC6R2LqZJ+L3rLhXJQ1K1Zc=


***Option 2: Decrypted Message***

Encrypted Message: U2FsdGVkX1+Hg/3q1e4YpC6R2LqZJ+L3rLhXJQ1K1Zc=
Decrypted Message: Hello Camellia Encryption!


***Option 3: Exit***

Exiting...


*Note: Encrypted text differs each run because CBC mode uses a random IV internally.*

## 3. Time and Space Complexity
|Function|	Time Complexity|	Space Complexity|	Explanation|
|:-------|:----------------|:-------------------|:-------------|
|encrypt_camellia|	O(L)|	O(L)|	L = length of plaintext. Base64 encoding + encryption scales linearly.|
|decrypt_camellia|	O(L)|	O(L)|	Base64 decode + decryption scales linearly.|
|subprocess call overhead|	O(1)|	O(1)|	Minor overhead for spawning external process.|
|Overall Program|	O(L)|	O(L)|	Dominated by encryption/decryption of message length.|

**Notes:**

- CBC mode requires processing blocks sequentially → still O(L) overall.

- L = plaintext length in bytes.

- Base64 adds ~33% space overhead for ciphertext representation.

## 4. Summary

- Uses Camellia-256-CBC via OpenSSL for secure encryption.

- Padding/truncating ensures 32-byte key compatibility.

- CBC mode ensures random IV → unique ciphertexts for repeated messages.

- Menu system allows interactive display of encrypted/decrypted text.

- Time and space complexity scale linearly with plaintext size.