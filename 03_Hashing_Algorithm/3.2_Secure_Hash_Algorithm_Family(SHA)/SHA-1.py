#Secure_Hash_Algorithm-1(SHA-1)

import hashlib

def sha1_hash(text):
    sha1 = hashlib.sha1()  # Create SHA-1 hash object
    sha1.update(text.encode())  # Hash the input text
    return sha1.hexdigest()  # Return hash as a hex string

# Example usage
if __name__ == "__main__":
    text = input("Enter text to hash with SHA-1: ")
    hashed_text = sha1_hash(text)
    print("SHA-1 Hash:", hashed_text)


# #HMAC-SHA1
# import hmac

# def hmac_sha1(key, message):
#     return hmac.new(key.encode(), message.encode(), hashlib.sha1).hexdigest()

# # Example
# print(hmac_sha1("secretkey", "HelloWorld"))  # Secure HMAC-SHA1
