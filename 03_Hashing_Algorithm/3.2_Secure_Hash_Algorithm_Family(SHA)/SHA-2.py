#Secure_Hash_Algorithm-2(SHA-2)

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
