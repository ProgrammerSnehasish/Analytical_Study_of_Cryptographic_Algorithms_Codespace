from Crypto.Hash import CMAC
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# User input
message = input("Enter your message: ").encode()

# Key generation (128-bit AES key)
key = get_random_bytes(16)  # 16 bytes = 128 bits

# CMAC generation
c = CMAC.new(key, ciphermod=AES)
c.update(message)
mac = c.hexdigest()

print("CMAC (Hex):", mac)
