def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

# Encrypt message using public key (e, n)
def encrypt(m, e, n):
    return power(m, e, n)

# Decrypt message using private key (d, n)
def decrypt(c, d, n):
    return power(c, d, n)

if __name__ == "__main__":
    try:
        print("Enter Public Key (e, n):")
        e = int(input("e: "))
        n = int(input("n: "))

        print("Enter Private Key (d, n):")
        d = int(input("d: "))

        M = int(input("Enter the message (integer less than n): "))

        if M >= n:
            print(f"Error: Message must be less than n ({n})")
        else:
            C = encrypt(M, e, n)
            print(f"\nEncrypted Message: {C}")

            decrypted = decrypt(C, d, n)
            print(f"Decrypted Message: {decrypted}")

    except ValueError:
        print("Invalid input. Please enter integers only.")
