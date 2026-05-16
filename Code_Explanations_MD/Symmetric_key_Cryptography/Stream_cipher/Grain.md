# Grain Code
```python
def int_to_bits(n, width):
    return [int(b) for b in bin(n)[2:].zfill(width)]

def bits_to_int(bits):
    return int(''.join(map(str, bits)), 2)

def shift(register, feedback_bit):
    return [feedback_bit] + register[:-1]

def grain_feedback_lfsr(lfsr):
    # Feedback polynomial (example)
    return lfsr[0] ^ lfsr[13] ^ lfsr[23] ^ lfsr[38] ^ lfsr[51] ^ lfsr[62]

def grain_feedback_nfsr(nfsr, lfsr):
    # Nonlinear feedback function (illustrative, supports up to index 91)
    return nfsr[0] ^ nfsr[26] ^ nfsr[56] ^ (nfsr[91] & lfsr[0]) ^ (nfsr[3] & nfsr[67])

def grain_filter(nfsr, lfsr):
    return nfsr[1] ^ lfsr[3] ^ (nfsr[5] & lfsr[7]) ^ (nfsr[10] & lfsr[12])

def generate_keystream(key, iv, length):
    if len(key) != 128 or len(iv) != 128:
        raise ValueError("Key and IV must be 128 bits after padding.")

    lfsr = iv.copy()
    nfsr = key.copy()

    for _ in range(160):  # initialization
        z = grain_filter(nfsr, lfsr)
        nfsr_fb = grain_feedback_nfsr(nfsr, lfsr) ^ z
        lfsr_fb = grain_feedback_lfsr(lfsr) ^ z
        nfsr = shift(nfsr, nfsr_fb)
        lfsr = shift(lfsr, lfsr_fb)

    keystream = []
    for _ in range(length * 8):  # generate 1 bit per iteration
        z = grain_filter(nfsr, lfsr)
        keystream.append(z)
        nfsr = shift(nfsr, grain_feedback_nfsr(nfsr, lfsr))
        lfsr = shift(lfsr, grain_feedback_lfsr(lfsr))

    return keystream

def bytes_to_bits(data):
    return [bit for byte in data for bit in int_to_bits(byte, 8)]

def bits_to_bytes(bits):
    return bytes(bits_to_int(bits[i:i+8]) for i in range(0, len(bits), 8))

def grain_encrypt(key_str, iv_str, plaintext):
    key_bits = bytes_to_bits(key_str.encode('utf-8')[:10])       # 80 bits
    key_bits += [0] * (128 - len(key_bits))                      # pad to 128

    iv_bits = bytes_to_bits(iv_str.encode('utf-8')[:8])          # 64 bits
    iv_bits += [1] * (128 - len(iv_bits))                        # pad to 128

    plaintext_bits = bytes_to_bits(plaintext.encode('utf-8'))

    keystream = generate_keystream(key_bits, iv_bits, len(plaintext))
    cipher_bits = [p ^ k for p, k in zip(plaintext_bits, keystream)]
    return bits_to_bytes(cipher_bits)

def grain_decrypt(key_str, iv_str, ciphertext):
    key_bits = bytes_to_bits(key_str.encode('utf-8')[:10])       # 80 bits
    key_bits += [0] * (128 - len(key_bits))

    iv_bits = bytes_to_bits(iv_str.encode('utf-8')[:8])          # 64 bits
    iv_bits += [1] * (128 - len(iv_bits))

    ciphertext_bits = bytes_to_bits(ciphertext)
    keystream = generate_keystream(key_bits, iv_bits, len(ciphertext))
    plain_bits = [c ^ k for c, k in zip(ciphertext_bits, keystream)]
    return bits_to_bytes(plain_bits).decode('utf-8', errors='ignore')

# === User Input ===
key_input = input("Enter 10-character key (80-bit): ")
iv_input = input("Enter 8-character IV (64-bit): ")
plaintext_input = input("Enter plaintext to encrypt: ")

# Encryption
cipher = grain_encrypt(key_input, iv_input, plaintext_input)
print("\nCiphertext (hex):", cipher.hex())

# Decryption
decrypted = grain_decrypt(key_input, iv_input, cipher)
print("Decrypted text:", decrypted)
```

## 🧩 Overview

Grain Stream Cipher is a synchronous stream cipher.
It uses:

- A Linear Feedback Shift Register (LFSR) for linear state evolution.

- A Nonlinear Feedback Shift Register (NFSR) for nonlinear state evolution.

- A filter function that mixes both registers to generate keystream bits.

Encryption/Decryption use XOR:

𝐶𝑖 = 𝑃𝑖⊕𝐾𝑖 and 𝑃𝑖 = 𝐶𝑖⊕𝐾𝑖

where
𝑃𝑖: plaintext bit
𝐾𝑖: keystream bit
𝐶𝑖: ciphertext bit

## ⚙️ Code Breakdown
### 1. Utility Functions
**(a) int_to_bits(n, width)**

Converts an integer into a list of bits (MSB → LSB).
```python
def int_to_bits(n, width):
    return [int(b) for b in bin(n)[2:].zfill(width)]
```
Used for: byte → bits conversion.

**Time complexity:** O(width)
**Space complexity:** O(width)

**(b) bits_to_int(bits)**
Converts a list of bits back to an integer.
```python
def bits_to_int(bits):
    return int(''.join(map(str, bits)), 2)
```

**Time complexity:** O(n)
**Space complexity:** O(n)

**(c) shift(register, feedback_bit)**

Performs a left shift of the register, inserting a new feedback bit.
```python
def shift(register, feedback_bit):
    return [feedback_bit] + register[:-1]
```
Equivalent to: moving bits by 1 position each cycle.
**Time complexity:** O(n)
**Space complexity:** O(n)

### 2. Feedback and Filter Functions
**(a) grain_feedback_lfsr(lfsr)**

Implements the linear feedback polynomial:
```python
def grain_feedback_lfsr(lfsr):
    return lfsr[0] ^ lfsr[13] ^ lfsr[23] ^ lfsr[38] ^ lfsr[51] ^ lfsr[62]
```

XOR of selected tap bits simulates LFSR’s linear recurrence relation.

**Time complexity:** O(1)

**Space complexity:** O(1)

**(b) grain_feedback_nfsr(nfsr, lfsr)**

Implements the nonlinear feedback:
```python
def grain_feedback_nfsr(nfsr, lfsr):
    return nfsr[0] ^ nfsr[26] ^ nfsr[56] ^ (nfsr[91] & lfsr[0]) ^ (nfsr[3] & nfsr[67])
```

Introduces nonlinearity by using AND and XOR combinations.

Strengthens cipher against linear cryptanalysis.

**Time complexity:** O(1)

**Space complexity:** O(1)

**(c) grain_filter(nfsr, lfsr)**

Computes the output keystream bit:
```python
def grain_filter(nfsr, lfsr):
    return nfsr[1] ^ lfsr[3] ^ (nfsr[5] & lfsr[7]) ^ (nfsr[10] & lfsr[12])
```

Mixes bits from both registers to produce pseudorandom output.

**Time complexity:** O(1)

**Space complexity:** O(1)

## 3. Keystream Generation
generate_keystream(key, iv, length)

This is the heart of the cipher — it generates the keystream bits.

Steps:

- Initialize LFSR with IV (Initialization Vector).

- Initialize NFSR with Key bits.

Initialization phase (160 rounds):

- Mix LFSR & NFSR to eliminate biases.

- Update both using feedbacks and filter output.

Keystream generation phase:

For each bit of plaintext:

Compute output bit 
𝑧=𝑓(𝑁𝐹𝑆𝑅, 𝐿𝐹𝑆𝑅)

Append 
𝑧 to keystream.

Shift both registers using feedback.
```python
for _ in range(length * 8):
    z = grain_filter(nfsr, lfsr)
    keystream.append(z)
    nfsr = shift(nfsr, grain_feedback_nfsr(nfsr, lfsr))
    lfsr = shift(lfsr, grain_feedback_lfsr(lfsr))
```

## 🧮 Complexity:

|Operation |Time|	Space|
|:------|:------|:-------|
|Initialization (160 rounds)	|O(160) → O(1)|	O(1)|
|Keystream generation|	O(n)	|O(n)|

Total: O(n) time and O(n) space
(where n = number of plaintext bytes × 8 bits)

### 4. Bit Conversion Helpers

bytes_to_bits(data) → Convert bytes → bit list

bits_to_bytes(bits) → Convert bit list → bytes

Both operate in O(n) time and space (n = total bits).

### 5. Encryption and Decryption

Both encryption and decryption are identical (since XOR is symmetric).

**(a) Encryption**
```python
def grain_encrypt(key_str, iv_str, plaintext):
    key_bits = bytes_to_bits(key_str.encode('utf-8')[:10])
    key_bits += [0] * (128 - len(key_bits))

    iv_bits = bytes_to_bits(iv_str.encode('utf-8')[:8])
    iv_bits += [1] * (128 - len(iv_bits))

    plaintext_bits = bytes_to_bits(plaintext.encode('utf-8'))
    keystream = generate_keystream(key_bits, iv_bits, len(plaintext))
    cipher_bits = [p ^ k for p, k in zip(plaintext_bits, keystream)]
    return bits_to_bytes(cipher_bits)
```

Steps:

- Convert key (80 bits) → padded 128 bits.

- Convert IV (64 bits) → padded 128 bits.

- Convert plaintext to bits.

Generate keystream of equal length.

XOR plaintext bits with keystream bits → ciphertext.

**(b) Decryption**

Same steps, except:

Input is ciphertext.

XOR ciphertext bits with keystream → plaintext bits.

plain_bits = [c ^ k for c, k in zip(ciphertext_bits, keystream)]


## 🧮 Complexity (both encryption and decryption):

|Stage|	Time|	Space|
|:------|:----|:-----|
|Bit conversion|	O(n)|	O(n)|
|Keystream generation|	O(n)|	O(n)|
|XOR operation|	O(n)|	O(n)|
|Total|	O(n)|	O(n)|

## 🧠 Algorithm Summary

|Component|	Description|	Type|	Complexity|
|:------|:-----------|:----------------|:------|
|LFSR	|Linear feedback shift register|	Linear recurrence|	O(1) per bit|
|NFSR	|Nonlinear feedback shift register|	Nonlinear Boolean|	O(1) per bit|
|Filter Function	|Combines LFSR + NFSR|	Boolean mixing|	O(1) per bit|
|Encryption|	XOR of plaintext and keystream|	Bitwise	|O(n)|
|Decryption|	Same as encryption	|Bitwise	|O(n)|

## 🔒 Security Insights

**✅ Strengths:**

Uses nonlinear feedback, improving resistance to algebraic and correlation attacks.

Initialization step ensures diffusion between key and IV.

XOR encryption makes it fast and simple.

**⚠️ Weakness (in simplified version):**

The true Grain v1 cipher uses longer registers (80/160 bits) and more complex functions.

Here, the polynomial and feedback logic are truncated for demonstration.

## 📊 Example Execution

Input:

Key:  mysecretk
IV:   myivdata
Plaintext: Hello


Output:

Ciphertext (hex): 3a7f5c...
Decrypted text: Hello

## 🧮 Overall Complexity Summary
|Stage|	Operation|	Time|	Space|
|Key & IV setup|	Conversion + padding|	O(1)|	O(1)|
|Initialization|	160 rounds|	O(1)|	O(1)|
|Keystream generation|	Per-bit feedback & shift|	O(n)|	O(n)|
|Encryption/Decryption|	XOR|	O(n)|	O(n)|
|Total|	—|	O(n)|	O(n)|