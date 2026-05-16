#Secure_Hash_Algorithm-3(SHA-3)

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
