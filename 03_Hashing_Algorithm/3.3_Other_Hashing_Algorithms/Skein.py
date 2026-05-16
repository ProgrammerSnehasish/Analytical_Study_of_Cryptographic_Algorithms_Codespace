# Skein is a flexible cryptographic hash function that supports variable digest sizes, was a SHA-3 finalist,
# and is built around a tweakable block cipher (Threefish).

import skein

# Take user input
message = input("Enter the message to hash using Skein-512: ")
data = message.encode('utf-8')

# Create a Skein-512 hash object with a 512-bit output
hash_obj = skein.skein512()
# hash_obj = skein.skein256()   # For Skein-256
# hash_obj = skein.skein1024()  # For Skein-1024
# hash_obj = skein.skein512(digest_bits=384)  # 384-bit output

hash_obj.update(data)

# Print the hash in hexadecimal form
print("Skein-512 Digest:", hash_obj.hexdigest())
