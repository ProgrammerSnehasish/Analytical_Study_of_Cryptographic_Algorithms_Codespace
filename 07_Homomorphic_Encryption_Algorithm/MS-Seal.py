#MS Seal

#Microsoft SEAL itself is written in C++ and does not have an official Python API. However, TenSEAL is built on top of SEAL and allows you to work with homomorphic encryption in Python.


import tenseal as ts # type: ignore

# Create a TenSEAL context for encryption
context = ts.context(
    ts.SCHEME_TYPE.BFV,
    poly_modulus_degree=8192,
    plain_modulus=1032193,  # Required parameter
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2**40

# User input: Enter numbers
user_input = input("Enter numbers separated by spaces: ")
vector = list(map(int, user_input.split()))

# Encrypt data
encrypted_vector = ts.bfv_vector(context, vector)

# User choice for operation
print("\nChoose an operation:")
print("1. Add encrypted vector to itself")
print("2. Multiply encrypted vector by 2")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    encrypted_result = encrypted_vector + encrypted_vector
elif choice == "2":
    encrypted_result = encrypted_vector * 2
else:
    print("Invalid choice. Exiting.")
    exit()

# Decrypt result
plain_result = encrypted_result.decrypt()
print("Decrypted result:", plain_result)



# import seal

# # Setup SEAL Encryption Parameters
# parms = seal.EncryptionParameters(seal.scheme_type.BFV)
# poly_modulus_degree = 4096  # Degree of the polynomial modulus
# parms.set_poly_modulus_degree(poly_modulus_degree)
# parms.set_coeff_modulus(seal.CoeffModulus.BFVDefault(poly_modulus_degree))
# parms.set_plain_modulus(1024)

# # Create SEALContext
# context = seal.SEALContext(parms)

# # Key Generation
# keygen = seal.KeyGenerator(context)
# public_key = keygen.public_key()
# secret_key = keygen.secret_key()
# relin_keys = keygen.relin_keys()

# # Encryptor, Evaluator, and Decryptor
# encryptor = seal.Encryptor(context, public_key)
# evaluator = seal.Evaluator(context)
# decryptor = seal.Decryptor(context, secret_key)

# # Encoder for integer values
# encoder = seal.IntegerEncoder(context)

# # Function to encrypt a number
# def encrypt_number(num):
#     plain = encoder.encode(num)
#     encrypted = encryptor.encrypt(plain)
#     return encrypted

# # Function to decrypt a number
# def decrypt_number(encrypted):
#     decrypted_plain = decryptor.decrypt(encrypted)
#     decrypted_num = encoder.decode(decrypted_plain)
#     return decrypted_num

# while True:
#     print("\n🔹 Microsoft SEAL Homomorphic Encryption")
#     print("1. Encrypt Numbers")
#     print("2. Perform Encrypted Addition")
#     print("3. Perform Encrypted Multiplication")
#     print("4. Decrypt a Value")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         num = int(input("Enter a number to encrypt: "))
#         encrypted_num = encrypt_number(num)
#         print(f"🔒 Encrypted Value: {encrypted_num}")

#     elif choice == "2":
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
        
#         enc1 = encrypt_number(num1)
#         enc2 = encrypt_number(num2)

#         enc_result = evaluator.add(enc1, enc2)
#         decrypted_result = decrypt_number(enc_result)

#         print(f"🔓 Decrypted Sum: {num1} + {num2} = {decrypted_result}")

#     elif choice == "3":
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
        
#         enc1 = encrypt_number(num1)
#         enc2 = encrypt_number(num2)

#         enc_result = evaluator.multiply(enc1, enc2)
#         decrypted_result = decrypt_number(enc_result)

#         print(f"🔓 Decrypted Product: {num1} × {num2} = {decrypted_result}")

#     elif choice == "4":
#         num = int(input("Enter a number to encrypt and decrypt: "))
#         enc_num = encrypt_number(num)
#         decrypted_num = decrypt_number(enc_num)
#         print(f"🔒 Encrypted: {enc_num}")
#         print(f"🔓 Decrypted: {decrypted_num}")

#     elif choice == "5":
#         print("Exiting... 🔚")
#         break

#     else:
#         print("❌ Invalid choice. Try again!")
