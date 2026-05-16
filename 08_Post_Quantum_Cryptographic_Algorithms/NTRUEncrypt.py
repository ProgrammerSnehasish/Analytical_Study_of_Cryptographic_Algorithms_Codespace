import numpy as np

# Parameters
N = 5   # Polynomial degree
p = 3   # Small modulus (message space)
q = 32  # Large modulus (ciphertext space)

# Key Generation (toy example)
def generate_keys():
    f = np.array([1, -1, 0, 1, -1], dtype=int)  # Private polynomial
    g = np.array([1, 0, -1, 1, 0], dtype=int)   # Public polynomial
    Fp = np.array([1, 1, 0, -1, 1], dtype=int)  # Approximate inverse mod p
    h = np.mod(np.convolve(f, g)[:N], q)        # Public key
    return f, g, Fp, h

# Encryption
def encrypt(message, h):
    r = np.array([1, 0, -1, 0, 1], dtype=int)  # Random small poly
    e = np.mod(np.convolve(r, h)[:N] + message, q)
    return e

# Decryption
def decrypt(ciphertext, f, Fp):
    a = np.mod(np.convolve(ciphertext, f)[:N], q)
    decrypted_message = np.mod(np.convolve(a, Fp)[:N], p)
    return decrypted_message

# ----------- MAIN -----------
print(f"\nEnter a binary message of {N} values (0 or 1 only):")
user_input = input(f"Separate values with spaces (e.g., 1 0 1 0 1): ")

# Parse input
try:
    message_list = [int(x) % p for x in user_input.strip().split()]
    if len(message_list) != N:
        raise ValueError("Input length mismatch")
except:
    print("Invalid input. Please enter exactly 5 binary values separated by spaces.")
    exit()

message = np.array(message_list, dtype=int)

# Key generation
f, g, Fp, h = generate_keys()

# Encryption & Decryption
ciphertext = encrypt(message, h)
decrypted_message = decrypt(ciphertext, f, Fp)

# Results
print("\n--- NTRU Encrypt Demo (Simplified) ---")
print("Original Message: ", message.tolist())
print("Public Key (h):   ", h.tolist())
print("Ciphertext:       ", ciphertext.tolist())
print("Decrypted Message:", decrypted_message.tolist())
