# The implementation below is not the actual SEAL algorithm as designed by Rogaway and Coppersmith, but a simplified illustrative 
# simulation that demonstrates the key idea — generating a long pseudorandom keystream from a key and XORing it with plaintext.

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
