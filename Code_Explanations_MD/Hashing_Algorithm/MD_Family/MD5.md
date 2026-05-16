# MD5 Code
```python
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
```

## ⚙️ Algorithmic Approach
|Step|	Description|
|:---|:------------|
|Step 1|	Take input message from the user.|
|Step 2|	Convert the message into bytes using UTF-8 encoding.|
|Step 3|	Initialize an MD5 hashing object using Python’s hashlib.md5().|
|Step 4|	Feed the message bytes to the hash object using update().|
|Step 5|	Generate the hash digest using hexdigest() to obtain the hexadecimal output.|
|Step 6|	Print the resulting 128-bit hash.|

## 🧠 About the MD5 Algorithm

Designer: Ronald Rivest (1991)
Digest Length: 128 bits (16 bytes)
Block Size: 512 bits (64 bytes)
Output Format: 32-character hexadecimal string
Security: Broken — Vulnerable to collision and preimage attacks.
Common Uses (Today): File checksum verification and legacy systems (not for security).

## 🧾 Example Demo
Input:
Enter the message to hash using MD5: cybersecurity

Output:
MD5 Hash: f4d47f0c1eb16b516eec2dc54a7e15bb

Another Example:
Enter the message to hash using MD5: hello

Output:
MD5 Hash: 5d41402abc4b2a76b9719d911017c592

## ⏱️ Time and Space Complexity
|Operation|	Time Complexity|	Space Complexity|	Description|
|:--------|:---------------|:-------------------|:-------------|
|Message Encoding|	O(n)|	O(n)|	Converts input string to bytes.|
|Hash Computation|	O(n)|	O(1)|	MD5 processes input in 512-bit (64-byte) chunks.|
|Digest Generation|	O(1)|	O(1)|	Converts final hash to hexadecimal string.|
|Overall|	O(n)|	O(n)|	Linear in the length of input message.|

## ⚠️ Security Note

MD5 is cryptographically broken and should not be used for password storage or cryptographic purposes.
It remains useful for checksums, data integrity verification, and educational demonstrations.