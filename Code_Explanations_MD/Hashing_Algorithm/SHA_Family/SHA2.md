# SHA2 Code
```python
import hashlib

def sha2_hash(data, algorithm="sha256"):
    """Generate SHA-2 hash for the given data."""
    hash_func = getattr(hashlib, algorithm, None)
    if hash_func is None:
        raise ValueError("Invalid SHA-2 algorithm. Choose from 'sha224', 'sha256', 'sha384', or 'sha512'.")
    
    hashed = hash_func(data.encode()).hexdigest()
    return hashed

def main():
    print("SHA-2 Hash Generator")
    data = input("Enter data to hash: ")

    print("\nSelect SHA-2 variant:")
    print("1. SHA-224")
    print("2. SHA-256")
    print("3. SHA-384")
    print("4. SHA-512")
    
    choice = input("Enter choice (1-4): ")
    algorithms = {"1": "sha224", "2": "sha256", "3": "sha384", "4": "sha512"}
    
    if choice in algorithms:
        hashed_value = sha2_hash(data, algorithms[choice])
        print(f"\n{algorithms[choice].upper()} Hash: {hashed_value}")
    else:
        print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()
```

## ⚙️ Algorithmic Approach
|Step|	Description|
|:---|:------------|
|Step 1|	Prompt the user to enter a message (data).|
|Step 2|	Display options to choose among SHA-2 variants — SHA-224, SHA-256, SHA-384, and SHA-512.|
|Step 3|	Based on the user’s choice, select the corresponding algorithm using hashlib.|
|Step 4|	Convert the input data to bytes using UTF-8 encoding.|
|Step 5|	Apply the chosen SHA-2 hashing algorithm to compute the digest.|
|Step 6|	Output the resulting hash in hexadecimal format.|

## 🧠 About the SHA-2 Algorithm Family
|Variant|	Digest Size|	Security Strength|	Typical Use|
|:------|:-------------|:--------------------|:------------|
|SHA-224|	224 bits (28 bytes)|	Moderate|	Legacy applications|
|SHA-256|	256 bits (32 bytes)|	Strong|	Common default choice|
|SHA-384|	384 bits (48 bytes)|	Very strong|	Digital signatures, SSL|
|SHA-512|	512 bits (64 bytes)|	Very strong|	High-security systems, blockchain|

*Key Facts:*

- Developed by the NSA and published by NIST in 2001.

- SHA-2 is not vulnerable to known collision attacks like SHA-1.

- It’s widely used in TLS, SSL, Bitcoin, and digital certificates.

## 🧾 Example Demos
✅ Example 1: SHA-256

Input:

Enter data to hash: hello
Enter choice (1-4): 2


Output:

SHA-256 Hash: `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`

✅ Example 2: SHA-512

Input:

Enter data to hash: cybersecurity
Enter choice (1-4): 4


Output:

SHA-512 Hash:   `a558ca4a27e0487f85f1b09f5a4a35f7b5f55a6174baf519b00f6a3de13f4e5a78ef7d6cbf1b63135e6a8d76462f1e1f6f4e0e2b02c1e6f23e4ff0f912c89ab6`

## ⏱️ Time and Space Complexity Analysis
|Operation|	Time Complexity|	Space Complexity|	Description|
|:--------|:---------------|:-------------------|:-------------|
|Encoding Input|	O(n)|	O(n)|	Converts user input into bytes.|
|Hash Function (Compression)|	O(n)|	O(1)|	Processes data in 512-bit blocks.|
|Digest Conversion|	O(1)|	O(1)|	Converts binary hash to hex string.|
|Overall Complexity|	O(n)|	O(n)|	Linear with respect to input length.|

## 🔐 Security Notes

- SHA-2 remains cryptographically secure as of today.

- Resistant to collision and preimage attacks.

- Recommended for password hashing, digital signatures, and message authentication.

- For even higher security, use SHA-3 (Keccak family).