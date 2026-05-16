from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Step 1: Take user input
message = input("Enter the message to sign using RSA: ").encode('utf-8')

# Step 2: Generate RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Step 3: Sign the message using PKCS#1 v1.5 padding and SHA-256
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Step 4: Get public key from private key
public_key = private_key.public_key()

# Step 5: Display the signature
print("\nSignature (hex):", signature.hex())

# Step 6: Verify the signature
try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Signature verification: Valid")
except:
    print("Signature verification: Invalid")


# Export private key (PEM)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Export public key (PEM)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Print or save to file
print("\nPrivate Key:\n", private_pem.decode())
print("\nPublic Key:\n", public_pem.decode())
