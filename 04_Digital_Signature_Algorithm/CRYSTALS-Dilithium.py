# CRYSTALS-Dilithium is a post-quantum digital signature algorithm selected by NIST for standardization.
# It is based on lattice-based cryptography, providing strong security even against quantum computers.

# Python does not support CRYSTALS-Dilithium natively. However, you can use the pqcrypto or pycrystals libraries, 
# which provide Python bindings to Dilithium implementations

from pqcrypto.sign import dilithium3
from pqcrypto.utils import randombytes
# from pqcrypto.sign import dilithium2   # NIST Level 2
# from pqcrypto.sign import dilithium5   # NIST Level 5 (highest)


# Step 1: Take user input
message = input("Enter the message to sign using CRYSTALS-Dilithium: ").encode('utf-8')

# Step 2: Generate keypair (public key and private key)
public_key, private_key = dilithium3.generate_keypair()

# Step 3: Sign the message
signature = dilithium3.sign(message, private_key)

# Step 4: Verify the signature
try:
    verified_message = dilithium3.open(signature, public_key)
    print("\nSignature verification: Valid")
    print("Verified Message:", verified_message.decode('utf-8'))
except Exception as e:
    print("Signature verification: Invalid")
    print("Error:", e)

# Step 5: Output signature and public key for inspection
print("\nSignature (hex):", signature.hex())

# CRYSTALS-Dilithium is one of the strongest and most efficient post-quantum digital signature schemes available.
# Using Python bindings like pqcrypto, you can securely generate, sign, and verify messages in a quantum-safe way.