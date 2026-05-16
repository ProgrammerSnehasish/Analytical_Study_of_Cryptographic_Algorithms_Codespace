from Crypto.Hash import MD2

def md2_hash_user_input():
    # Take input from user
    message = input("Enter the message to hash using MD2: ")
    
    # Convert message to bytes
    message_bytes = message.encode('utf-8')
    
    # Create MD2 hash object and update it with the message
    hash_obj = MD2.new()
    hash_obj.update(message_bytes)
    
    # Get the digest (hash value) in hexadecimal
    digest = hash_obj.hexdigest()
    
    # Print the hash
    print(f"MD2 Hash of the message: {digest}")

# Run the function
md2_hash_user_input()
