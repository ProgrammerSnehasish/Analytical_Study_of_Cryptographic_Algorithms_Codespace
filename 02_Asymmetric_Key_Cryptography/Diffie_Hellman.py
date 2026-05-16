# Diffie-Hellman Key Exchange using user input

def power(base, exponent, mod):
    """Modular exponentiation: (base^exponent) % mod"""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

# User input for prime number (p) and primitive root (g)
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root modulo p (g): "))

# Private keys (chosen secretly)
a = int(input("Enter private key for User A (a): "))
b = int(input("Enter private key for User B (b): "))

# Calculate public keys
A = power(g, a, p)  # A = g^a mod p
B = power(g, b, p)  # B = g^b mod p

print(f"User A Public Key (A): {A}")
print(f"User B Public Key (B): {B}")

# Generate shared secret keys
shared_key_A = power(B, a, p)  # (B^a) mod p
shared_key_B = power(A, b, p)  # (A^b) mod p

print(f"Shared secret key computed by User A: {shared_key_A}")
print(f"Shared secret key computed by User B: {shared_key_B}")

if shared_key_A == shared_key_B:
    print("Key exchange successful! Shared key is established.")
else:
    print("Key exchange failed. Shared keys do not match.")
