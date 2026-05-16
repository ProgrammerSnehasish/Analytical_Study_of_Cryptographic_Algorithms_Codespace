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
