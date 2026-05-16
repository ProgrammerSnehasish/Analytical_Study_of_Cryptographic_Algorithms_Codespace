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
