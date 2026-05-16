import random
import math

# Function to compute L(x, n) = (x - 1) // n
def L(x, n):
    return (x - 1) // n

# Function to compute modular inverse
def modinv(a, m):
    return pow(a, -1, m)

# Key generation
def generate_keys():
    p = 17  # Use larger primes in production
    q = 23
    n = p * q
    g = n + 1
    λ = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
    μ = modinv(L(pow(g, λ, n**2), n), n)
    return (n, g), (λ, μ)

# Encryption
def encrypt(m, public_key):
    n, g = public_key
    r = random.randint(1, n - 1)
    while math.gcd(r, n) != 1:
        r = random.randint(1, n - 1)
    c = (pow(g, m, n**2) * pow(r, n, n**2)) % (n**2)
    return c

# Decryption
def decrypt(c, private_key, public_key):
    n, g = public_key
    λ, μ = private_key
    m = (L(pow(c, λ, n**2), n) * μ) % n
    return m

# -------- MAIN --------
print("Enter two text-value pairs.")

# First input
text1 = input("Enter first text label: ")
val1 = int(input("Enter value for first text: "))

# Second input
text2 = input("\nEnter second text label: ")
val2 = int(input("Enter value for second text: "))

# Key generation
public_key, private_key = generate_keys()

# Encrypt values
c1 = encrypt(val1, public_key)
c2 = encrypt(val2, public_key)

# Homomorphic addition
c_sum = (c1 * c2) % (public_key[0] ** 2)
decrypted_sum = decrypt(c_sum, private_key, public_key)

# Output
print("\n--- Paillier Homomorphic Encryption: Text + Value ---")
print(f"{text1}: {val1} (Encrypted: {c1})")
print(f"{text2}: {val2} (Encrypted: {c2})")
print(f"Decrypted homomorphic sum ({text1} + {text2}): {decrypted_sum}")
