import hashlib

def md5_hash():
    # Take user input
    message = input("Enter the message to hash using MD5: ")

    # Convert to bytes
    message_bytes = message.encode('utf-8')

    # Create hash object
    hash_object = hashlib.md5()

    # Update with the message
    hash_object.update(message_bytes)

    # Get hexadecimal digest
    digest = hash_object.hexdigest()

    print(f"MD5 Hash: {digest}")

# Run the function
md5_hash()
