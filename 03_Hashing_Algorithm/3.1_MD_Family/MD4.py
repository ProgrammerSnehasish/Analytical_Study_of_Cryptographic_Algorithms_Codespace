from Crypto.Hash import MD4

def md4_hash():
    # User input
    message = input("Enter a message to hash using MD4: ")
    
    # Encode message to bytes
    message_bytes = message.encode('utf-8')
    
    # Create MD4 hash object
    hash_obj = MD4.new()
    hash_obj.update(message_bytes)
    
    # Get the hexadecimal digest
    digest = hash_obj.hexdigest()
    
    print(f"MD4 Hash: {digest}")

# Run the function
md4_hash()
