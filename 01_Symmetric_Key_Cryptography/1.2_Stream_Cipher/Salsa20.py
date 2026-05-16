from Crypto.Cipher import Salsa20
import os

def salsa20_encrypt(key: bytes, plaintext: str) -> tuple[bytes, bytes]:
    """Encrypt plaintext using Salsa20 and return nonce and ciphertext"""
    cipher = Salsa20.new(key=key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return cipher.nonce, ciphertext

def salsa20_decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> str:
    """Decrypt ciphertext using Salsa20 and return plaintext"""
    cipher = Salsa20.new(key=key, nonce=nonce)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode('utf-8')

# === User Input ===
key_input = input("Enter a 32-byte (256-bit) key: ")
if len(key_input) != 32:
    raise ValueError("Key must be exactly 32 characters (256 bits).")

plaintext_input = input("Enter the plaintext to encrypt: ")

# Convert key to bytes
key = key_input.encode('utf-8')

# Encrypt
nonce, ciphertext = salsa20_encrypt(key, plaintext_input)
print("\nNonce (hex):", nonce.hex())
print("Encrypted (hex):", ciphertext.hex())

# Decrypt
decrypted = salsa20_decrypt(key, nonce, ciphertext)
print("\nDecrypted plaintext:", decrypted)
