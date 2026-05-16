import hashlib
import os
import binascii

def scrypt_derive_key(password: str, salt: bytes, n: int = 2**14, r: int = 8, p: int = 1, key_len: int = 32) -> bytes:
    """Derive a cryptographic key using scrypt"""
    password_bytes = password.encode('utf-8')
    return hashlib.scrypt(password_bytes, salt=salt, n=n, r=r, p=p, dklen=key_len)

# === User Input ===
password_input = input("Enter your password: ")

use_custom_salt = input("Use custom salt? (y/n): ").strip().lower()
if use_custom_salt == 'y':
    salt_input = input("Enter salt (ASCII): ")
    salt = salt_input.encode('utf-8')
else:
    salt = os.urandom(16)
    print("Generated random salt (hex):", salt.hex())

# Optional: Parameters
key_len_input = input("Enter key length in bytes (default 32): ").strip()
key_len = int(key_len_input) if key_len_input else 32

# === Key Derivation ===
derived_key = scrypt_derive_key(password_input, salt, key_len=key_len)

# === Output ===
print("\nDerived key (hex):", binascii.hexlify(derived_key).decode())
