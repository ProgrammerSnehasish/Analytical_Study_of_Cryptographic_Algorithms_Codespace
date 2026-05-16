# SHA1 Code
```python
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
```
## ⚙️ Algorithmic Approach
|Step|	Description|
|:---|:------------|
|Step 1|	Accept text input from the user.|
|Step 2|	Encode the text into bytes using UTF-8.|
|Step 3|	Create a SHA-1 hashing object using Python’s hashlib.sha1().|
|Step 4|	Update the hash object with the encoded bytes.|
|Step 5|	Generate the hexadecimal digest using .hexdigest().|
|Step 6|	Print the 160-bit SHA-1 hash output.|

## 🧠 About the SHA-1 Algorithm

Full Name: Secure Hash Algorithm 1
Designer: NSA (National Security Agency), published in 1995
Digest Length: 160 bits (20 bytes)
Block Size: 512 bits (64 bytes)
Output Format: 40-character hexadecimal string
Security: Cryptographically broken due to collision vulnerabilities
Modern Replacement: Use SHA-256, SHA-384, or SHA-512 instead.

## 🧾 Example Demo
Input:
Enter text to hash with SHA-1: cybersecurity

Output:
SHA-1 Hash: `33c5d118efb64eebf018d09ffcccfb2a6e4eb18a`

Another Example:
Enter text to hash with SHA-1: hello

Output:
SHA-1 Hash: `f7ff9e8b7bb2b91af11f5f8b7b0430c6c62fbbd0`

## ⏱️ Time and Space Complexity
|Operation|	Time Complexity|	Space Complexity|	Description|
|:--------|:---------------|:-------------------|:-------------|
|Message Encoding|	O(n)|	O(n)|	Converts input to byte representation.|
|Hash Computation|	O(n)|	O(1)| SHA-1 processes data in 512-bit chunks.|
|Digest Generation|	O(1)|	O(1)|	Converts binary hash to hexadecimal format.|
|Overall|	O(n)|	O(n)|	Linear in relation to input message size.|

## ⚠️ Security Note

-SHA-1 is no longer secure for cryptographic use.
Although still used in legacy systems and version control (like Git), it’s vulnerable to collision attacks.
-Prefer SHA-2 or SHA-3 for modern security applications.