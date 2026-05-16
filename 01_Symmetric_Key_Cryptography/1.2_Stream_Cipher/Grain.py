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
