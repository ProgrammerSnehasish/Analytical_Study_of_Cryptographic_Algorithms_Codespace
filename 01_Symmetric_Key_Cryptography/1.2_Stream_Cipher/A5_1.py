# These are simplified software simulations meant for academic understanding. 
# Both A5/1 and A5/2 are cryptographically broken and not recommended for actual secure communications.

# The A5/2 cipher uses four LFSRs with a more deterministic clocking mechanism, but it's even weaker than A5/1. 
# If you want to simulate A5/2, I can extend the code similarly — but for practical and academic analysis, A5/1 is more widely studied.

class LFSR:
    def __init__(self, length, taps, clock_bit):
        self.register = [0] * length
        self.taps = taps
        self.clock_bit = clock_bit

    def feedback(self):
        return sum(self.register[tap] for tap in self.taps) % 2

    def shift(self):
        fb = self.feedback()
        self.register = [fb] + self.register[:-1]

    def get_clock_bit(self):
        return self.register[self.clock_bit]

def majority(a, b, c):
    return (a & b) | (a & c) | (b & c)

def a5_1_initialize(key_bits):
    R1 = LFSR(19, [13, 16, 17, 18], 8)
    R2 = LFSR(22, [20, 21], 10)
    R3 = LFSR(23, [7, 20, 21, 22], 10)

    # Load key bits (64-bit key)
    for i in range(64):
        bit = key_bits[i]
        R1.register[0] ^= bit
        R2.register[0] ^= bit
        R3.register[0] ^= bit
        R1.shift()
        R2.shift()
        R3.shift()

    return R1, R2, R3

def a5_1_keystream(R1, R2, R3, n_bits):
    stream = []
    for _ in range(n_bits):
        m = majority(R1.get_clock_bit(), R2.get_clock_bit(), R3.get_clock_bit())
        if R1.get_clock_bit() == m:
            R1.shift()
        if R2.get_clock_bit() == m:
            R2.shift()
        if R3.get_clock_bit() == m:
            R3.shift()
        z = R1.register[-1] ^ R2.register[-1] ^ R3.register[-1]
        stream.append(z)
    return stream

def str_to_bits(s):
    return [int(b) for byte in s.encode('utf-8') for b in f"{byte:08b}"]

def bits_to_str(bits):
    return bytes(int("".join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8)).decode('utf-8', errors='ignore')

def xor_bits(a, b):
    return [x ^ y for x, y in zip(a, b)]

# === User Input ===
key_input = input("Enter a 64-bit key (8 characters): ")
plaintext_input = input("Enter the plaintext to encrypt: ")

if len(key_input) != 8:
    raise ValueError("Key must be exactly 8 characters (64 bits).")

key_bits = str_to_bits(key_input)
plaintext_bits = str_to_bits(plaintext_input)

# A5/1 encryption
R1, R2, R3 = a5_1_initialize(key_bits)
ks = a5_1_keystream(R1, R2, R3, len(plaintext_bits))
cipher_bits = xor_bits(plaintext_bits, ks)

# Decryption (same process, stream cipher)
R1_d, R2_d, R3_d = a5_1_initialize(key_bits)
ks_d = a5_1_keystream(R1_d, R2_d, R3_d, len(cipher_bits))
decrypted_bits = xor_bits(cipher_bits, ks_d)

# === Output ===
print("\nEncrypted (binary):", ''.join(map(str, cipher_bits)))
print("Encrypted (hex):", hex(int(''.join(map(str, cipher_bits)), 2))[2:])
print("Decrypted text:", bits_to_str(decrypted_bits))
