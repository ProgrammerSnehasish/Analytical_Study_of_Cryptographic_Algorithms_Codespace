# RC4 Code
```python
def ksa(key):
    """Key Scheduling Algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def prga(S, plaintext_length):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = j = 0
    keystream = []

    for _ in range(plaintext_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])

    return keystream

def rc4_encrypt(plaintext, key):
    """Encrypt or decrypt using RC4"""
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S, len(plaintext))
    plaintext = [ord(c) for c in plaintext]

    cipher = [p ^ k for p, k in zip(plaintext, keystream)]
    return cipher

def rc4_decrypt(cipher, key):
    """Decrypt RC4 ciphertext"""
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S, len(cipher))

    decrypted = [c ^ k for c, k in zip(cipher, keystream)]
    return ''.join([chr(c) for c in decrypted])

# === User Input ===
key_input = input("Enter the key: ")
plaintext_input = input("Enter the plaintext to encrypt: ")

# Encryption
ciphertext = rc4_encrypt(plaintext_input, key_input)
print("\nEncrypted (hexadecimal representation):")
print(' '.join(format(c, '02x') for c in ciphertext))

# Decryption
decrypted_text = rc4_decrypt(ciphertext, key_input)
print("\nDecrypted plaintext:")
print(decrypted_text)
```

## 🧩 Overview

RC4 (Rivest Cipher 4) — designed by Ron Rivest (1987) — is a stream cipher.
It generates a pseudorandom keystream which is XORed with plaintext to produce ciphertext.

Encryption and decryption are identical operations, since:

𝐶𝑖 = 𝑃𝑖⊕𝐾𝑖 and 𝑃𝑖=𝐶𝑖⊕𝐾𝑖

where

𝑃𝑖: plaintext byte
𝐾𝑖: keystream byte
𝐶𝑖: ciphertext byte

## ⚙️ Code Breakdown
### 1. Key Scheduling Algorithm (KSA)
```python
def ksa(key):
    key_length = len(key)
    S = list(range(256))  # Initialize permutation array
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap
    return S
```
**🔹 Algorithm**

- Initialize an array S of 256 integers (0–255).

- Use the key to scramble this array through modular addition and swaps.

- Output S, the permutation state, used by PRGA to generate keystream.

Mathematical Expression:
𝑆𝑖 = 𝑖 for 0 ≤ 𝑖 < 256
𝑗 = (𝑗+𝑆𝑖+𝐾𝑖 mod∣𝐾∣)mod256
swap(𝑆𝑖,𝑆𝑗)

**🔹 Purpose**

- This process mixes the key into the state array.

- It ensures diffusion so that small key changes cause large keystream changes.

**🔹 Complexity**
|Operation| Time|	Space|
|:--------|:----|:-------|
|Loop (256 iterations)|	O(256) = O(1)|	O(256) = O(1)|

KSA always runs in constant time because the loop size is fixed (256 bytes).

## 2. Pseudo-Random Generation Algorithm (PRGA)
```python
def prga(S, plaintext_length):
    i = j = 0
    keystream = []

    for _ in range(plaintext_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])

    return keystream
```
**🔹 Algorithm**

Initialize i and j as 0.

- Repeatedly update i and j indices.

- Swap elements in S.

- Output a byte from S based on (S[i] + S[j]) % 256.

This produces a pseudorandom keystream.

Formula:
    𝑖 =(𝑖+1)mod256
    𝑗=(𝑗+𝑆[𝑖])mod256
swap(𝑆[𝑖],𝑆[𝑗])
    𝐾=𝑆[(𝑆[𝑖]+𝑆[𝑗])mod256]

**🔹 Complexity**
|Operation|	Time|	Space|
|:--------|:----|:-------|
|Loop (plaintext_length iterations)|	O(n)|	O(n)|

Here, n = length of plaintext.
For every byte, the algorithm performs constant operations.

## 3. RC4 Encryption
```python
def rc4_encrypt(plaintext, key):
    key = [ord(c) for c in key]               # Convert key to ASCII codes
    S = ksa(key)                              # Initialize S
    keystream = prga(S, len(plaintext))       # Generate keystream
    plaintext = [ord(c) for c in plaintext]   # Convert plaintext to integers
    cipher = [p ^ k for p, k in zip(plaintext, keystream)]  # XOR
    return cipher
```
🔹 Steps

- Convert key and plaintext into integer lists.

- Run KSA → obtain the permutation S.

- Run PRGA → produce keystream bytes.

XOR plaintext bytes with keystream bytes → ciphertext.

Formula:
𝐶𝑖=𝑃𝑖⊕𝐾𝑖

**🔹 Complexity**
|Stage|	Time|	Space|
|:----|:----|:-------|
|KSA|	O(1)|	O(1)|
|PRGA|	O(n)|	O(n)|
|XOR (encryption)|	O(n)|	O(n)|
|Total|	O(n)|	O(n)|
## 4. RC4 Decryption
```python
def rc4_decrypt(cipher, key):
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S, len(cipher))
    decrypted = [c ^ k for c, k in zip(cipher, keystream)]
    return ''.join([chr(c) for c in decrypted])
```
**🔹 Steps**

- Re-run KSA and PRGA using the same key.

- Generate identical keystream.

- XOR ciphertext with keystream to recover plaintext.

Formula:

𝑃𝑖=𝐶𝑖⊕𝐾𝑖

Since XOR is self-inverse, encryption and decryption are symmetric.

**🔹 Complexity**

Same as encryption:

**Time**: O(n)

**Space**: O(n)

## 5. User Interaction & Output
```python
key_input = input("Enter the key: ")
plaintext_input = input("Enter the plaintext to encrypt: ")

ciphertext = rc4_encrypt(plaintext_input, key_input)
print(' '.join(format(c, '02x') for c in ciphertext))

decrypted_text = rc4_decrypt(ciphertext, key_input)
print("\nDecrypted plaintext:", decrypted_text)
```

### Example Execution

Enter the key: secret
Enter the plaintext to encrypt: HELLO

Encrypted (hexadecimal representation):
fa c4 23 1b 92

Decrypted plaintext:
HELLO

## 🧮 Complexity Summary
|Stage|	Operation|	Time Complexity|	Space Complexity|
|:----|:---------|:----------|:------------------|
|KSA	|Initialize and permute S|	O(1)|	O(1)|
|PRGA|	Generate keystream|	O(n)|	O(n)|
|XOR (encryption/decryption)|	Bitwise XOR|	O(n)|	O(n)|
|Overall|	—|	O(n)|	O(n)|

*✅ Linear time complexity — excellent for real-time encryption.*
*⚠️ However, RC4 is cryptographically broken and no longer secure for modern use.*

## 🔐 Security Notes
|Aspect|	Description|
|:-----|:--------------|
|Strength|	Extremely fast, small code footprint.|
|Weakness|	Initial keystream bytes are biased. Predictable key scheduling leaks info.|
|Status|	Deprecated — not used in TLS, WPA3, or SSH anymore.|
|Modern Alternative|	ChaCha20 or AES-CTR (much stronger, constant-time secure).|

## 🧠 Summary
|Feature|	RC4 Implementation|
|:------|:--------------------|
|Cipher Type|	Stream Cipher|
|Key Size|	Variable (1–256 bytes)|
|State Array (S)|	256 bytes|
|Main Algorithms|	KSA (Key Scheduling), PRGA (Keystream Generation)|
|Encryption Rule|	Ciphertext = Plaintext XOR Keystream|
|Decryption Rule|	Plaintext = Ciphertext XOR Keystream|
|Time Complexity|	O(n)|
|Space Complexity|	O(n)|
|Security Status|	Deprecated (bias in keystream)|