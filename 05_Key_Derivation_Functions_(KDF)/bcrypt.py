import bcrypt

# === User Input: Password Entry ===
password = input("Enter your password: ").encode('utf-8')

# === Generate Salt and Hash Password ===
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

# === Display Results ===
print("\nHashed password (bcrypt):", hashed_password.decode())
print("Salt used (base64):", salt.decode())

# === Verification ===
verify_password = input("\nRe-enter password to verify: ").encode('utf-8')
if bcrypt.checkpw(verify_password, hashed_password):
    print("Password verified successfully.")
else:
    print("Password verification failed.")
