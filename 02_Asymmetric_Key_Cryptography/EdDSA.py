from cryptography.hazmat.primitives.asymmetric import ed25519

# Take message input from the user
user_input = input("Enter the message to sign using EdDSA (Ed25519): ")
message = user_input.encode()

# Generate Ed25519 private key
private_key = ed25519.Ed25519PrivateKey.generate()

# Sign the message
signature = private_key.sign(message)

# Get the corresponding public key
public_key = private_key.public_key()

# Verify the signature
try:
    public_key.verify(signature, message)
    print("Signature is valid.")
except Exception as e:
    print("Signature verification failed:", str(e))
