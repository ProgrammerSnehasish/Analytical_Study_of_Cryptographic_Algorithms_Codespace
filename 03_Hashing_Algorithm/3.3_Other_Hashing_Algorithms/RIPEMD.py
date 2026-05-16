# Python implementation of the RIPEMD-160 hash algorithm using the Crypto.Hash.RIPEMD module from the PyCryptodome library.
# This script accepts user input and returns the RIPEMD-160 hash digest.



from Crypto.Hash import RIPEMD

# Get input from user
user_input = input("Enter the message to hash using RIPEMD-160: ")

# Encode input to bytes
data = user_input.encode('utf-8')

# Create a RIPEMD-160 hash object
hash_obj = RIPEMD.new()
hash_obj.update(data)

# Print the hash in hexadecimal format
print("RIPEMD-160 Digest:", hash_obj.hexdigest())
