from blake3 import blake3

# Take user input
message = input("Enter the message to hash using BLAKE3: ")
data = message.encode('utf-8')

# Compute the hash
hash_obj = blake3()
hash_obj.update(data)

# Print the 256-bit (32-byte) digest
print("BLAKE3 Digest:", hash_obj.hexdigest())
