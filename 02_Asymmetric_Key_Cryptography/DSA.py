from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed

# Ask user for input message
user_input = input("Enter the message to sign using DSA: ")
message = user_input.encode()

# Generate DSA private key (2048 bits)
private_key = dsa.generate_private_key(key_size=2048)

# Sign the message
# Note: DSA requires pre-hashing the message for SHA256
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
hashed_message = digest.finalize()

signature = private_key.sign(
    message,
    hashes.SHA256()
)

# Get public key from private key
public_key = private_key.public_key()

# Verify the signature
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    print("Signature is valid.")
except Exception as e:
    print("Signature verification failed:", str(e))
