import secrets
import hashlib

# Parameters (Toy values for understanding; not secure!)
q = 3329  # Prime modulus
n = 256   # Polynomial degree (simplified)
eta = 2   # Noise distribution parameter

def random_poly():
    return [secrets.randbelow(q) for _ in range(n)]

def add_poly(a, b):
    return [(x + y) % q for x, y in zip(a, b)]

def mul_poly(a, b):
    # Naive polynomial multiplication mod q (simplified, inefficient)
    res = [0] * (2 * n - 1)
    for i in range(n):
        for j in range(n):
            res[i + j] = (res[i + j] + a[i] * b[j]) % q
    return [res[i] for i in range(n)]  # truncate to n terms

# Key Generation
def kyber_keygen():
    s = random_poly()      # private key
    e = random_poly()      # error
    A = random_poly()      # public matrix (1D for demo)
    pk = add_poly(mul_poly(A, s), e)
    return pk, s

# Encapsulation
def kyber_encapsulate(pk):
    r = random_poly()
    e1 = random_poly()
    e2 = random_poly()
    u = add_poly(mul_poly(pk, r), e1)
    shared_secret = hashlib.sha3_256(str(e2).encode()).hexdigest()
    ciphertext = (u, e2)
    return ciphertext, shared_secret

# Decapsulation
def kyber_decapsulate(ciphertext, s):
    u, e2 = ciphertext
    v = mul_poly(u, s)
    shared_secret = hashlib.sha3_256(str(e2).encode()).hexdigest()
    return shared_secret

# Demo
pk, sk = kyber_keygen()
ciphertext, ss_enc = kyber_encapsulate(pk)
ss_dec = kyber_decapsulate(ciphertext, sk)

print("Shared secret (encapsulation):", ss_enc)
print("Shared secret (decapsulation):", ss_dec)
print("Match:", ss_enc == ss_dec)
