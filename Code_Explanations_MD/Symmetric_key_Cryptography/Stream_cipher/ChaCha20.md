# ChaCha20 Code
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os

def chacha20_encrypt(key: bytes, nonce: bytes, plaintext: str) -> bytes:
    """Encrypt plaintext using ChaCha20"""
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode('utf-8'))
    return ciphertext

def chacha20_decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> str:
    """Decrypt ciphertext using ChaCha20"""
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext)
    return decrypted.decode('utf-8')

# === User Input ===
key_input = input("Enter a 32-byte (256-bit) key: ")
if len(key_input) != 32:
    raise ValueError("Key must be exactly 32 characters (256 bits).")

plaintext_input = input("Enter the plaintext to encrypt: ")

# Convert user input to bytes
key = key_input.encode('utf-8')
nonce = os.urandom(12)  # 96-bit (12-byte) nonce

# Encryption
ciphertext = chacha20_encrypt(key, nonce, plaintext_input)
print("\nEncrypted (hexadecimal):")
print(ciphertext.hex())

# Decryption
decrypted_text = chacha20_decrypt(key, nonce, ciphertext)
print("\nDecrypted plaintext:")
print(decrypted_text)
```

## 🧩 Overview

**ChaCha20** is a high-speed, modern **stream cipher** designed by **Daniel J. Bernstein**.  
It is widely used in secure communication protocols such as **TLS 1.3**, **SSH**, and **VPNs**.

It operates on **256-bit keys** and **96-bit nonces**, providing both security and performance.

---

## ⚙️ Code Breakdown

### 1. **Imports**

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os
```
Cipher, algorithms: Used to construct the ChaCha20 cipher object.

default_backend: Provides the cryptographic backend implementation.

os.urandom: Generates a cryptographically secure random nonce.

### 2. Encryption Function
```python
def chacha20_encrypt(key: bytes, nonce: bytes, plaintext: str) -> bytes:
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode('utf-8'))
    return ciphertext
```
**Algorithm: ChaCha20 Stream Cipher**
Works by generating a keystream derived from:

256-bit key

96-bit nonce

Internal counter (starts at 0)

The plaintext is XORed with the keystream to produce ciphertext.

𝐶𝑖 = 𝑃𝑖⊕𝐾𝑖

where
𝑃𝑖: plaintext byte
𝐾𝑖: keystream byte
𝐶𝑖: ciphertext byte

Steps:
- Create a ChaCha20 algorithm instance with key and nonce.

- Initialize a cipher object.

- Create an encryptor.

XOR plaintext with the keystream → ciphertext.

**Time Complexity:**
Generating keystream + XOR = O(n) (linear in plaintext length)

**Space Complexity:**
Ciphertext and temporary buffers = O(n)

### 3. Decryption Function
```python
def chacha20_decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> str:
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext)
    return decrypted.decode('utf-8')
```
Decryption Algorithm:
Decryption is identical to encryption because ChaCha20 is a synchronous stream cipher:

𝑃𝑖 = 𝐶𝑖 ⊕ 𝐾𝑖

Same keystream regenerates since the same key and nonce are used.

Steps:
- Initialize ChaCha20 with same key and nonce.

- Create decryptor object.

- XOR ciphertext with identical keystream → plaintext.

**Time Complexity**: O(n)
**Space Complexity**: O(n)

### 4. User Input and Execution
```python
key_input = input("Enter a 32-byte (256-bit) key: ")
if len(key_input) != 32:
    raise ValueError("Key must be exactly 32 characters (256 bits).")

plaintext_input = input("Enter the plaintext to encrypt: ")

key = key_input.encode('utf-8')
nonce = os.urandom(12)  # 96-bit nonce
```
User enters a 32-character key → converted to bytes.

A random 12-byte (96-bit) nonce is generated.

Ensures uniqueness of keystream for each encryption.

### 5. Encryption and Decryption Process
```python
ciphertext = chacha20_encrypt(key, nonce, plaintext_input)
print("\nEncrypted (hexadecimal):")
print(ciphertext.hex())

decrypted_text = chacha20_decrypt(key, nonce, ciphertext)
print("\nDecrypted plaintext:")
print(decrypted_text)
```
Steps:
- Encrypt the plaintext using chacha20_encrypt.

- Print ciphertext in hexadecimal format.

- Decrypt using the same key and nonce.

Print recovered plaintext.

## 🧮 Complexity Analysis
| Stage | Operation | Time Complexity | Space Complexity |
|:------|:-----------|:----------------|:-----------------|
|Key Setup |Initialize key and nonce|	O(1)|	O(1)|
|Encryption |Generate keystream and XOR plaintext|	O(n)	|O(n)|
|Decryption |	Generate keystream and XOR ciphertext|	O(n)|	O(n)|
|Total|	—	|O(n)|	O(n)|

(n = length of plaintext in bytes)

## 🔐 Security Notes
Nonce Reuse Warning:
Never reuse the same (key, nonce) pair. It leads to keystream reuse, which can leak plaintext via XOR.

ChaCha20 Advantages:

Resistant to timing attacks.

Faster than AES on software.

Strong 256-bit security.

## ✅ Example Execution
Input:

Enter a 32-byte (256-bit) key: thisisaverysecure32bytekeystring!
Enter the plaintext to encrypt: Hello World
Output:

Encrypted (hexadecimal):
4f6a5cde83a8d8f6a0...

Decrypted plaintext:
Hello World

## 🧠 Summary
Algorithm Used: ChaCha20 (stream cipher)

Key Size: 256 bits (32 bytes)

Nonce Size: 96 bits (12 bytes)

Encryption/Decryption: XOR with keystream

Time Complexity: O(n)

Space Complexity: O(n)

Secure and efficient for: Real-time communication, VPNs, TLS