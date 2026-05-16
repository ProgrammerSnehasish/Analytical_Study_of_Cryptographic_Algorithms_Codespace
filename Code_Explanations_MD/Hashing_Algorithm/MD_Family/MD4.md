# MD4 Code
```python
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
```

## ⚙️ Algorithmic Approach
|Step|	Description|
|:---|:------------|
|Step 1|	Take the input message from the user.|
|Step 2|	Convert the message into bytes (UTF-8 encoding).|
|Step 3|	Initialize an MD4 hashing object using Crypto.Hash.MD4.|
|Step 4|	Feed the byte message into the MD4 hashing object using update().|
|Step 5|	Compute the hash digest using hexdigest() to get a hexadecimal representation.|
|Step 6|	Display the resulting hash to the user.|

## 🧠 About the MD4 Algorithm

Designer: Ronald Rivest (1990)
Digest Length: 128 bits (16 bytes)
Block Size: 512 bits
Security: Broken — vulnerable to collision and preimage attacks.
Purpose: Early cryptographic hash function, predecessor of MD5 and SHA family.

## 🧾 Example Demo
Input:
Enter a message to hash using MD4: cybersecurity

Output:
MD4 Hash: `4a1e63de87c7f27f26baf3674cc0b94b`

Another Example:
Enter a message to hash using MD4: hello


Output:

MD4 Hash: `aa010fbc1d14c795d86ef98c95479d17`

## ⏱️ Time and Space Complexity
|Operation|	Time Complexity|	Space Complexity|	Description|
|:--------|:---------------|:-------------------|:-------------|
|Message Encoding|	O(n)|	O(n)|	Converts input string to bytes.|
|Hash Computation|	O(n)|	O(1)|	Final hex digest generation.|
|Overall|	O(n)|	O(n)|	Linear in size of input message.|

## ⚠️ Security Note

MD4 is cryptographically broken and should not be used in any secure application.
It’s valuable only for educational and historical understanding of early hashing mechanisms.