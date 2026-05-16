from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives import serialization

# Step 1: Get message input from the user
message = input("Enter the message to sign using DSA: ").encode('utf-8')

# Step 2: Generate a DSA private key (default: 2048-bit key)
private_key = dsa.generate_private_key(key_size=2048)

# Step 3: Sign the message
signature = private_key.sign(message, hashes.SHA256())

# Step 4: Derive the public key
public_key = private_key.public_key()

# Step 5: Print the signature
print("\nSignature (hex):", signature.hex())

# Step 6: Verify the signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature verification: Valid")
except:
    print("Signature verification: Invalid")

# Export private key
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Export public key
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save to file or print
print(pem_private.decode())
print(pem_public.decode())

