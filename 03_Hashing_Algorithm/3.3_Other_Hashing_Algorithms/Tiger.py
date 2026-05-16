from tigerhash import tiger

# Take user input
message = input("Enter the message to hash using Tiger: ")
data = message.encode('utf-8')

# Compute the Tiger hash
digest = tiger(data)

# Display the digest in hexadecimal format
print("Tiger Digest:", digest.hex())