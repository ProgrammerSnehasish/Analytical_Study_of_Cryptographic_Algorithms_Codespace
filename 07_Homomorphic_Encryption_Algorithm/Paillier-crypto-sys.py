#Paillier Crypto System

import random
import gmpy2 # type: ignore

class Paillier:
    def __init__(self, key_size=512):
        self.key_size = key_size
        self.p, self.q = self.generate_prime(), self.generate_prime()
        self.n = self.p * self.q
        self.l = (self.p - 1) * (self.q - 1)
        self.g = self.n + 1
        self.mu = gmpy2.invert(self.l, self.n)
    
    def generate_prime(self):
        return gmpy2.next_prime(random.getrandbits(self.key_size // 2))

    def encrypt(self, message):
        if not (0 <= message < self.n):
            raise ValueError("Message must be in range [0, n)")
        r = random.randint(1, self.n - 1)
        c = (pow(self.g, message, self.n**2) * pow(r, self.n, self.n**2)) % (self.n**2)
        return c

    def decrypt(self, ciphertext):
        x = pow(ciphertext, self.l, self.n**2) - 1
        message = ((x // self.n) * self.mu) % self.n
        return int(message)

# User Interface
if __name__ == "__main__":
    paillier = Paillier()

    print("\nPaillier Cryptosystem")
    print("1. Encrypt a number")
    print("2. Decrypt a number")
    print("3. Homomorphic Addition")
    choice = input("Enter choice: ")

    if choice == "1":
        msg = int(input("Enter a number to encrypt: "))
        enc = paillier.encrypt(msg)
        print("Encrypted Message:", enc)

    elif choice == "2":
        enc = int(input("Enter encrypted number: "))
        dec = paillier.decrypt(enc)
        print("Decrypted Message:", dec)

    elif choice == "3":
        msg1 = int(input("Enter first number: "))
        msg2 = int(input("Enter second number: "))
        enc1 = paillier.encrypt(msg1)
        enc2 = paillier.encrypt(msg2)
        homomorphic_sum = (enc1 * enc2) % (paillier.n**2)  # Homomorphic addition
        dec_result = paillier.decrypt(homomorphic_sum)
        print("Encrypted Sum:", homomorphic_sum)
        print("Decrypted Sum:", dec_result)

    else:
        print("Invalid choice!")
