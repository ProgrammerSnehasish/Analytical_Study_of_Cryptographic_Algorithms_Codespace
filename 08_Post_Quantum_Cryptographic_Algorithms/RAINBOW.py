import numpy as np
from hashlib import sha256

# Simple finite field GF(2)
def gf2_add(x, y):
    return x ^ y

def gf2_dot(v1, v2):
    return sum([a & b for a, b in zip(v1, v2)]) % 2

# Generate a random quadratic polynomial system (simplified)
def generate_key(n=5, m=3):
    # Random quadratic coefficients a_ij and linear b_i, constant c_i
    private_key = {'a': np.random.randint(0, 2, (m, n, n)),
                   'b': np.random.randint(0, 2, (m, n)),
                   'c': np.random.randint(0, 2, m)}
    return private_key

# Evaluate the system P(x)
def evaluate(public_key, x):
    result = []
    for i in range(len(public_key['c'])):
        val = public_key['c'][i]
        for j in range(len(x)):
            val ^= public_key['b'][i][j] & x[j]
            for k in range(j, len(x)):
                val ^= public_key['a'][i][j][k] & x[j] & x[k]
        result.append(val)
    return result

# Simple signing: try random vectors until one matches hash
def sign(private_key, message, max_attempts=1000):
    hash_bits = [int(b) for b in bin(int(sha256(message.encode()).hexdigest(), 16))[2:].zfill(256)]
    target = hash_bits[:len(private_key['c'])]

    for _ in range(max_attempts):
        x = np.random.randint(0, 2, len(private_key['b'][0]))
        if evaluate(private_key, x) == target:
            return x.tolist()
    return None

# Verification
def verify(public_key, message, signature):
    hash_bits = [int(b) for b in bin(int(sha256(message.encode()).hexdigest(), 16))[2:].zfill(256)]
    target = hash_bits[:len(public_key['c'])]
    return evaluate(public_key, signature) == target

# Example usage
private_key = generate_key()
public_key = private_key  # In real Rainbow, this is obfuscated
msg = "post-quantum test"
sig = sign(private_key, msg)

if sig:
    print("Signature:", sig)
    print("Verified:", verify(public_key, msg, sig))
else:
    print("Signing failed.")
