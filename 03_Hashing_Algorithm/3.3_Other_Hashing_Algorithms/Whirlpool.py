from Crypto.Hash import Whirlpool

# Take user input
message = input("Enter the message to hash using Whirlpool: ")
data = message.encode('utf-8')

# Create Whirlpool hash object and update it with the data
hash_obj = Whirlpool.new()
hash_obj.update(data)

# Print the digest in hexadecimal format
print("Whirlpool Digest:", hash_obj.hexdigest())