import hashlib
import random

# Simulated parameters
def hash_to_key(shared_curve):
    return hashlib.sha256(str(shared_curve).encode()).hexdigest()

def generate_private_key():
    return random.randint(1, 1000)

def isogeny_map(curve, secret_key):
    # Simulate mapping curve with key (in real life this involves complex math)
    return (curve * secret_key) % 7919  # using a large prime modulus

# Setup: shared public base curve
base_curve = 1009

# Alice's key generation
alice_private = generate_private_key()
alice_public = isogeny_map(base_curve, alice_private)

# Bob's key generation
bob_private = generate_private_key()
bob_public = isogeny_map(base_curve, bob_private)

# Key exchange
alice_shared = isogeny_map(bob_public, alice_private)
bob_shared = isogeny_map(alice_public, bob_private)

# Both should derive the same shared key
alice_key = hash_to_key(alice_shared)
bob_key = hash_to_key(bob_shared)

print("Alice's Key:", alice_key)
print("Bob's Key:  ", bob_key)
print("Keys match: ", alice_key == bob_key)
