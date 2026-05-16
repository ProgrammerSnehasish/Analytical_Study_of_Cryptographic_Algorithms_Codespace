#TFHE

from concrete import fhe # type: ignore

# Define the encrypted function
@fhe.compiler({"x": "encrypted", "y": "encrypted"})
def encrypted_addition(x, y):
    return x + y  # Homomorphic addition

# Provide an inputset for compilation (Example: Numbers 0-100)
inputset = [(i, j) for i in range(100) for j in range(100)]
circuit = encrypted_addition.compile(inputset)  # Compile the function with inputset

while True:
    print("\n🔹 **TFHE Encryption Menu** 🔹")
    print("1️⃣  Encrypt numbers")
    print("2️⃣  Encrypt & Decrypt (Homomorphic Addition)")
    print("3️⃣  Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  
        # Encryption only
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        enc_x, enc_y = circuit.encrypt(x, y)
        print("\n🔒 Encrypted values:")
        print(f"🔹 Encrypted x: {enc_x}")
        print(f"🔹 Encrypted y: {enc_y}")

    elif choice == "2":  
        # Full flow: Encrypt → Compute → Decrypt
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        enc_x, enc_y = circuit.encrypt(x, y)
        enc_result = circuit.run(enc_x, enc_y)
        result = circuit.decrypt(enc_result)

        print("\n🔹 Homomorphic Encryption in Action 🔹")
        print(f"✅ You entered: {x} and {y}")
        print("🔒 Encrypting numbers... Done!")
        print("⚙️  Performing encrypted addition... Done!")
        print(f"🔓 Decrypted result: {result}")

    elif choice == "3":
        print("🚪 Exiting the program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")




