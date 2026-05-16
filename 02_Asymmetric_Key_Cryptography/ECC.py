from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from hashlib import sha256

# Function to compress elliptic curve public key
def compress(public_key):
    numbers = public_key.public_numbers()
    return hex(numbers.x) + hex(numbers.y % 2)[2:]

# Generate private and public keys
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()
print("\nYour Public Key (compressed):", compress(public_key))

# Encryption using ECC
def encrypt(msg, peer_public_key):
    ephemeral_private_key = ec.generate_private_key(ec.SECP256R1())
    ephemeral_public_key = ephemeral_private_key.public_key()
    shared_secret = ephemeral_private_key.exchange(ec.ECDH(), peer_public_key)
    secret_key = sha256(shared_secret).digest()
    ciphertext = bytes([m ^ secret_key[i % len(secret_key)] for i, m in enumerate(msg.encode())])
    return ephemeral_public_key, ciphertext

# Decryption using ECC
def decrypt(ciphertext, eph_pub_key, priv_key):
    shared_secret = priv_key.exchange(ec.ECDH(), eph_pub_key)
    secret_key = sha256(shared_secret).digest()
    plaintext = bytes([c ^ secret_key[i % len(secret_key)] for i, c in enumerate(ciphertext)])
    return plaintext.decode()

# --- USER INPUT SECTION ---
message = input("\nEnter a message to encrypt using ECC: ")

# Encryption
eph_pub_key, encrypted_msg = encrypt(message, public_key)
print("Encrypted Message (in bytes):", encrypted_msg)

# Decryption
decrypted_msg = decrypt(encrypted_msg, eph_pub_key, private_key)
print("Decrypted Message:", decrypted_msg)

