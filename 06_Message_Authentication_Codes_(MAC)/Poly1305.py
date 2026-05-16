from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Message to authenticate
message = input("Enter message: ").encode()

# Generate a 256-bit key
key = get_random_bytes(32)  # 32 bytes = 256 bits

# Create Poly1305 object
mac = Poly1305.new(key=key, cipher=AES)

# Update with message
mac.update(message)

# Generate MAC tag
tag = mac.hexdigest()

print("Poly1305 MAC Tag (Hex):", tag)
