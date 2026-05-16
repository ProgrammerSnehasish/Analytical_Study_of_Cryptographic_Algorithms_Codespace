# EdDSA (Edwards-curve Digital Signature Algorithm) is a modern digital signature scheme that offers high performance, strong security, 
# and resistance to side-channel attacks. It is based on twisted Edwards curves and operates deterministically,
# eliminating the risks associated with poor randomness in traditional schemes.

# One of the most widely used variants is Ed25519, which operates over the Curve25519 elliptic curve with a 256-bit key size. 
# It is standardized in RFC 8032.

from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature

# Step 1: Take message input from the user
message = input("Enter the message to sign using EdDSA (Ed25519): ").encode('utf-8')

# Step 2: Generate Ed25519 private key
private_key = ed25519.Ed25519PrivateKey.generate()

# Step 3: Sign the message
signature = private_key.sign(message)

# Step 4: Derive the public key
public_key = private_key.public_key()

# Step 5: Display the signature
print("\nEdDSA (Ed25519) Signature (hex):", signature.hex())

# Step 6: Verify the signature
try:
    public_key.verify(signature, message)
    print("Signature verification: Valid")
except InvalidSignature:
    print("Signature verification: Invalid")

from cryptography.hazmat.primitives import serialization

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

print("\nPrivate Key PEM:\n", private_pem.decode())
print("\nPublic Key PEM:\n", public_pem.decode())

# EdDSA, specifically Ed25519, offers a modern, efficient, and highly secure alternative to traditional signature schemes
# like RSA and ECDSA. Its deterministic nature and side-channel resistance make it a preferred choice in security-critical applications
# including secure messaging, SSH authentication, and blockchain systems.