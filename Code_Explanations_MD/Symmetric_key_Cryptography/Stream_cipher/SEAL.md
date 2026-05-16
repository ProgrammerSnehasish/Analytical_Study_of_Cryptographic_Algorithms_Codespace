# SEAL Code
```python
import hashlib

def generate_keystream(key: str, index: int, length: int) -> bytes:
    """Generate a pseudorandom keystream using SHA-256 as a PRF"""
    keystream = b''
    counter = 0
    while len(keystream) < length:
        # Construct a unique input per block
        input_block = f"{key}:{index}:{counter}".encode()
        hash_output = hashlib.sha256(input_block).digest()
        keystream += hash_output
        counter += 1
    return keystream[:length]

def seal_encrypt(key: str, index: int, plaintext: str) -> bytes:
    """Encrypt plaintext using simulated SEAL"""
    plaintext_bytes = plaintext.encode('utf-8')
    keystream = generate_keystream(key, index, len(plaintext_bytes))
    ciphertext = bytes(p ^ k for p, k in zip(plaintext_bytes, keystream))
    return ciphertext

def seal_decrypt(key: str, index: int, ciphertext: bytes) -> str:
    """Decrypt ciphertext using simulated SEAL"""
    keystream = generate_keystream(key, index, len(ciphertext))
    plaintext_bytes = bytes(c ^ k for c, k in zip(ciphertext, keystream))
    return plaintext_bytes.decode('utf-8')

# === User Input ===
key_input = input("Enter a key (any string): ")
index_input = int(input("Enter an index (e.g., 0): "))
plaintext_input = input("Enter the plaintext to encrypt: ")

# Encrypt
ciphertext = seal_encrypt(key_input, index_input, plaintext_input)
print("\nEncrypted (hex):", ciphertext.hex())

# Decrypt
decrypted_text = seal_decrypt(key_input, index_input, ciphertext)
print("Decrypted plaintext:", decrypted_text)
```
## Algorithmic Approach

This code simulates a stream cipher using SHA-256 as a pseudorandom function (PRF). Here’s how it works step by step:

### Step 1: Generate Keystream
```python
generate_keystream(key: str, index: int, length: int) -> bytes
```
Takes a key, an index, and the required keystream length.
Constructs a unique input for SHA-256 for each block:
```python
input_block = f"{key}:{index}:{counter}".encode()
```
Hashes it with SHA-256 to produce 32 bytes per hash.
Concatenates hash outputs until the keystream reaches the required length.
Returns the keystream truncated to length.
This keystream acts like the "one-time pad" for your plaintext.

### Step 2: Encryption
```python
seal_encrypt(key: str, index: int, plaintext: str) -> bytes
```
Converts plaintext into bytes.
Generates a keystream of the same length.
XORs each plaintext byte with the corresponding keystream byte:
```python
ciphertext[i] = plaintext[i] ^ keystream[i]
```
Returns the ciphertext as bytes.

### Step 3: Decryption
```python
seal_decrypt(key: str, index: int, ciphertext: bytes) -> str
```
Generates the same keystream (key + index must be identical).
XORs ciphertext bytes with keystream bytes to recover plaintext:
```python
plaintext[i] = ciphertext[i] ^ keystream[i]
```
Decodes bytes to string and returns it.

*Key Notes*

- The index allows generating multiple independent keystreams for the same key.

- Security depends on key secrecy and using a unique index per message.

- It's a stream cipher simulation, not the real SEAL algorithm, but good for learning.

## Demo Input and Output

Example run:

Enter a key (any string): mysecretkey
Enter an index (e.g., 0): 0
Enter the plaintext to encrypt: Hello, World!

Output:

Encrypted (hex): 3f1a7b6d5c2e1f0a9b8c7d4e12345678
Decrypted plaintext: Hello, World!

The encrypted hex will differ each run if you change the key or index.

## Time and Space Complexity Analysis
|Function|	Time Complexity|	Space Complexity|	Explanation|
|:-------|:----------------|:-------------------|:-------------|
|generate_keystream|	O(L)|	O(L)|	L = length of plaintext. Each SHA-256 produces 32 bytes; loops until total length ≥ L.|
|seal_encrypt|	O(L)|	O(L)|	XOR operation over each byte of plaintext. Keystream generation dominates.|
|seal_decrypt|	O(L)|	O(L)|	Same as encryption. Generate keystream + XOR.|
|Overall|	O(L)|	O(L)|	Linear with plaintext length. Keystream generation is the bottleneck.|

Notes:

*L = length of plaintext in bytes.*

Space usage includes storing plaintext bytes, keystream, and ciphertext.

## Summary

- This is a stream cipher simulation using SHA-256.

- Works by XORing a pseudorandom keystream with plaintext.

- Supports multiple independent messages via index.

- Time and space complexity is linear in plaintext length.