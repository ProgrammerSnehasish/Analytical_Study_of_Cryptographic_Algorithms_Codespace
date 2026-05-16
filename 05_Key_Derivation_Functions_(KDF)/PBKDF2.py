import hashlib
import os
import binascii

def pbkdf2_derive_key(password: str, salt: bytes, iterations: int = 100000, key_len: int = 32, hash_name: str = 'sha256') -> bytes:
    """Derive a cryptographic key from a password using PBKDF2"""
    password_bytes = password.encode('utf-8')
    key = hashlib.pbkdf2_hmac(hash_name, password_bytes, salt, iterations, dklen=key_len)
    return key

# === User Input ===
password_input = input("Enter your password: ")

use_custom_salt = input("Use custom salt? (y/n): ").strip().lower()
if use_custom_salt == 'y':
    salt_input = input("Enter salt (as ASCII): ")
    salt = salt_input.encode('utf-8')
else:
    salt = os.urandom(16)
    print("Generated random salt (hex):", salt.hex())

iterations_input = input("Enter iteration count (default 100000): ").strip()
iterations = int(iterations_input) if iterations_input else 100000

key_len_input = input("Enter key length in bytes (default 32): ").strip()
key_len = int(key_len_input) if key_len_input else 32

# === Key Derivation ===
derived_key = pbkdf2_derive_key(password_input, salt, iterations, key_len)

# === Output ===
print("\nDerived key (hex):", binascii.hexlify(derived_key).decode())
