# SHA3 Code
```python
import hashlib

def sha3_hash(data, algorithm="sha3_256"):
    """Generate SHA-3 hash for the given data."""
    hash_func = getattr(hashlib, algorithm, None)
    if hash_func is None:
        raise ValueError("Invalid SHA-3 algorithm. Choose from 'sha3_224', 'sha3_256', 'sha3_384', or 'sha3_512'.")
    
    hashed = hash_func(data.encode()).hexdigest()
    return hashed

def main():
    print("SHA-3 Hash Generator")
    data = input("Enter data to hash: ")

    print("\nSelect SHA-3 variant:")
    print("1. SHA3-224")
    print("2. SHA3-256")
    print("3. SHA3-384")
    print("4. SHA3-512")
    
    choice = input("Enter choice (1-4): ")
    algorithms = {"1": "sha3_224", "2": "sha3_256", "3": "sha3_384", "4": "sha3_512"}
    
    if choice in algorithms:
        hashed_value = sha3_hash(data, algorithms[choice])
        print(f"\n{algorithms[choice].upper()} Hash: {hashed_value}")
    else:
        print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()
```

## ⚙️ Algorithmic Approach
|Step|	Description|
|:---|:------------|
|Step 1|	Prompt the user to enter data to hash.|
|Step 2|	Display the available SHA-3 variants — SHA3-224, SHA3-256, SHA3-384, and SHA3-512.|
|Step 3|	Get the user’s choice and map it to the correct SHA-3 algorithm.|
|Step 4|	Convert the input string into bytes using UTF-8 encoding.|
|Step 5|	Use Python’s hashlib to compute the SHA-3 hash of the data.|
|Step 6|	Display the resulting hexadecimal hash value.|

## 🧠 About the SHA-3 Algorithm Family
|Variant|	Digest Size|	Security Strength|	Description|
|:-------|:------------|:--------------------|:------------|
|SHA3-224|	224 bits (28 bytes)|	Moderate|	Compact digest, legacy support|
|SHA3-256|	256 bits (32 bytes)|	Strong|	Balanced for most modern uses|
|SHA3-384|	384 bits (48 bytes)|	Very strong|	Used in advanced crypto systems|
|SHA3-512|	512 bits (64 bytes)|	Very strong|	For highest-security environments|

## 🔍 Key Facts:

- Standardized by NIST in 2015 after a public competition (Keccak algorithm by Guido Bertoni et al.).

- Structurally different from SHA-2 — based on a sponge construction instead of Merkle–Damgård.

- Resistant to length-extension and collision attacks that affect SHA-2.

- Future-proof — ideal for high-integrity, long-term security systems.

## 🧾 Example Demos
✅ Example 1: SHA3-256

Input:

Enter data to hash: hello
Enter choice (1-4): 2


Output:

SHA3_256 Hash: `3338be694f50c5f338814986cdf0686453a888b84f424d792af4b9202398f392`

✅ Example 2: SHA3-512

Input:

Enter data to hash: cybersecurity
Enter choice (1-4): 4


Output:

SHA3_512 Hash: `73cfb0b0289e5de7c8e2c4824fbb5ab23d92b6fa9e9ff8c1d90f64c3045b4a5c0b1a6a5fa9ec94e9c42ee97edb5e449bc2c671a8a217cbf3db43f6e9a0ce2da4`

## ⏱️ Time and Space Complexity
|Operation|	Time Complexity|	Space Complexity|	Description|
|:--------|:---------------|:-------------------|:-------------|
|Encoding Input|	O(n)|	O(n)|	Converts user input to byte sequence.|
|SHA-3 Absorbing Phase|	O(n)|	O(1)|	Processes input data into the sponge state.|
|SHA-3 Squeezing Phase|	O(1)|	O(1)|	Extracts fixed-length hash output.|
|Overall|	O(n)|	O(n)|	Linear complexity with respect to message length.|

## 🔐 Security Notes

- SHA-3 is not an upgrade or replacement for SHA-2, but a different cryptographic family.

- It is immune to known SHA-1/SHA-2 weaknesses (e.g., collision and length-extension).

- Recommended for blockchain, password storage, and high-integrity digital signatures.

- Use SHA3-256 for balance between performance and security.