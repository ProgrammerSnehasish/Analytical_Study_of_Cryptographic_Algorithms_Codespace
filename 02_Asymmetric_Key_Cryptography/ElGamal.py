import random
from math import gcd

# Generate key such that it is coprime with q
def gen_key(q):
    key = random.randint(10**10, q - 1)
    while gcd(q, key) != 1:
        key = random.randint(10**10, q - 1)
    return key

# Fast modular exponentiation
def power(a, b, c):
    x = 1
    y = a % c
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c
        y = (y * y) % c
        b //= 2
    return x

# Encrypt the message
def encrypt(msg, q, h, g):
    en_msg = []
    k = gen_key(q)  # Sender's private key
    s = power(h, k, q)
    p = power(g, k, q)
    print("Ephemeral Key (g^k):", p)
    print("Shared Secret (h^k mod q):", s)

    for ch in msg:
        en_msg.append(s * ord(ch))
    return en_msg, p

# Decrypt the message
def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for val in en_msg:
        dr_msg.append(chr(val // h))
    return ''.join(dr_msg)

# Main driver with user input
def main():
    msg = input("Enter message to encrypt using ElGamal: ")
    print("Original Message:", msg)

    # Choose a large prime q
    q = random.randint(10**20, 10**21)  # Keep within safe integer range
    g = random.randint(2, q - 1)

    key = gen_key(q)       # Receiver's private key
    h = power(g, key, q)   # h = g^a mod q (Receiver's public key)

    print("\nPublic parameters:")
    print("Large prime (q):", q)
    print("Generator (g):", g)
    print("Public key (h = g^a mod q):", h)

    # Encrypt
    en_msg, p = encrypt(msg, q, h, g)
    print("\nEncrypted Message:", en_msg)

    # Decrypt
    decrypted_msg = decrypt(en_msg, p, key, q)
    print("\nDecrypted Message:", decrypted_msg)

if __name__ == "__main__":
    main()
