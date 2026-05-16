from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate AES key (128-bit)
key = get_random_bytes(16)  # 16 bytes = 128 bits

# Generate a random IV (nonce)
iv = get_random_bytes(12)  # 12 bytes (96 bits) recommended for GCM/GMAC

# Message to authenticate (as AAD - not encrypted)
message = input("Enter message to authenticate: ").encode()

# Create AES cipher in GCM mode
cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

# Provide message as Associated Authenticated Data (AAD)
cipher.update(message)

# Finalize and get the GMAC tag
tag = cipher.digest()

print("GMAC Tag (Hex):", tag.hex())
