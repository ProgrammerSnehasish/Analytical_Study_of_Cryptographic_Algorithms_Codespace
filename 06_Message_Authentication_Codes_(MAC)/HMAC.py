import hmac
import hashlib

# User Input
key = input("Enter secret key: ").encode()
message = input("Enter message: ").encode()

# Create HMAC object
hmac_obj = hmac.new(key, message, hashlib.sha256)

# Print the generated HMAC
print("HMAC (Hex):", hmac_obj.hexdigest())
