# Falcon (Fast-Fourier Lattice-based Compact Signatures over NTRU) is a post-quantum digital signature algorithm that was 
# selected by NIST as an alternative candidate in the third round of the post-quantum cryptography standardization process.
# It is based on lattice cryptography using the NTRU lattice structure and achieves both compact signatures and high security,
# even against quantum adversaries.

from pqcrypto.sign import falcon512
from pqcrypto.utils import randombytes

# Get message from user
message = input("Enter the message to sign using Falcon-512: ").encode('utf-8')

# Generate Falcon key pair
public_key, private_key = falcon512.generate_keypair()

# Sign the message
signature = falcon512.sign(message, private_key)

# Verify the signature
try:
    verified_message = falcon512.open(signature, public_key)
    print("Signature verification: Valid")
    print("Verified Message:", verified_message.decode())
except Exception as e:
    print("Signature verification: Invalid")
    print("Error:", e)

# Display signature
print("Signature (hex):", signature.hex())


# It uses Fast Fourier Sampling and requires high-precision floating-point operations, which makes it more complex 
# to implement securely compared to lattice-based schemes like Dilithium. However, its efficiency in communication overhead 
# and verification speed make it a compelling candidate for post-quantum applications.