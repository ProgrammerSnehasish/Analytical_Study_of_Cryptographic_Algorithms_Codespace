from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization

# Step 1: Get user input
message = input("Enter the message to sign using ECDSA: ").encode('utf-8')

# Step 2: Generate ECDSA private key (using SECP256R1 curve)
private_key = ec.generate_private_key(ec.SECP256R1())

# Step 3: Sign the message
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# Step 4: Get the public key from private key
public_key = private_key.public_key()

# Step 5: Print the signature
print("\nECDSA Signature (hex):", signature.hex())

# Step 6: Verify the signature
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("Signature verification: Valid")
except InvalidSignature:
    print("Signature verification: Invalid")

# Export private key
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Export public key
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Display the keys
print("\nPrivate Key PEM:\n", private_pem.decode())
print("\nPublic Key PEM:\n", public_pem.decode())

