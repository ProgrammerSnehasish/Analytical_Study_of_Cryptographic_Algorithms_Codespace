import hashlib

# Take user input
message = input("Enter the message to hash using BLAKE2b: ")
data = message.encode('utf-8')

# Create BLAKE2b hash object (512-bit digest by default)
hash_obj = hashlib.blake2b()
hash_obj.update(data)

# Display the hash in hexadecimal form
print("BLAKE2b Digest:", hash_obj.hexdigest())