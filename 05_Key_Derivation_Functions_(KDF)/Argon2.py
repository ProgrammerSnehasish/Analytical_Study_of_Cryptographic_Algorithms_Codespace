from argon2 import PasswordHasher, exceptions

# === Configure Argon2 Hasher ===
ph = PasswordHasher(
    time_cost=2,      # Number of iterations
    memory_cost=65536, # Memory usage in kibibytes (64 MB)
    parallelism=2,     # Number of parallel threads
    hash_len=32,       # Length of the derived key
    salt_len=16        # Salt size in bytes
)

# === User Input ===
password = input("Enter your password: ")

# === Hashing ===
hashed_password = ph.hash(password)
print("\nHashed password (Argon2):", hashed_password)

# === Verification ===
verify_password = input("\nRe-enter password to verify: ")

try:
    ph.verify(hashed_password, verify_password)
    print("Password verified successfully.")
except exceptions.VerifyMismatchError:
    print("Password verification failed.")
