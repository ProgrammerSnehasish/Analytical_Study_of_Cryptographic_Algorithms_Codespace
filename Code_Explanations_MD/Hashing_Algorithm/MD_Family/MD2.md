# MD2 Code
```python
from Crypto.Hash import MD2

def md2_hash_user_input():
    # Take input from user
    message = input("Enter the message to hash using MD2: ")
    
    # Convert message to bytes
    message_bytes = message.encode('utf-8')
    
    # Create MD2 hash object and update it with the message
    hash_obj = MD2.new()
    hash_obj.update(message_bytes)
    
    # Get the digest (hash value) in hexadecimal
    digest = hash_obj.hexdigest()
    
    # Print the hash
    print(f"MD2 Hash of the message: {digest}")

# Run the function
md2_hash_user_input()
```

# MD2 Hash Algorithm Analysis

## 🔹 Algorithmic Approach

1. **User Input:**
   - The program takes a plaintext message as input from the user.

2. **Encoding:**
   - The input string is encoded into bytes using UTF-8 encoding because the MD2 algorithm operates on byte data.

3. **Hash Object Creation:**
   - An MD2 hash object is created using `MD2.new()` from the `Crypto.Hash` module.

4. **Hash Update:**
   - The message bytes are passed to the hash object using `.update()` method, which processes the input data.

5. **Digest Generation:**
   - The final 128-bit (16-byte) hash is generated using `.hexdigest()`, which converts the binary digest into a readable hexadecimal string.

6. **Output:**
   - The hexadecimal digest (MD2 hash value) is printed as output.

---

## 🧮 Demo Input & Output

### **Input:**
```
Enter the message to hash using MD2: HelloWorld
```

### **Processing:**
- Convert to bytes → `b'HelloWorld'`
- Apply MD2 hashing → Generates 16-byte hash.

### **Output:**
```
MD2 Hash of the message: 1c8f1e6a94aaa7145210bf90bb52871a
```

---

## ⚙️ Time and Space Complexity Analysis

| Operation | Description | Time Complexity | Space Complexity |
|------------|--------------|------------------|------------------|
| Encoding Input | Convert string to bytes | O(n) | O(n) |
| Hash Update | Process message in 16-byte blocks | O(n) | O(1) |
| Digest Computation | Generate final 128-bit hash | O(1) | O(1) |
| **Overall** | **MD2 Hashing Process** | **O(n)** | **O(1)** |

🧠 **Explanation:**
- The MD2 algorithm processes input data block-by-block (16 bytes at a time).
- The runtime grows linearly with input length → **O(n)**.
- Since only fixed-size buffers are used, space requirement remains constant → **O(1)**.

---

## 🧩 Summary
- **Algorithm:** MD2 (Message Digest 2)
- **Hash Output Size:** 128 bits (16 bytes)
- **Deterministic:** Yes (same input → same hash)
- **Irreversible:** Cannot derive input from hash
- **Collision Resistance:** Weak (MD2 is obsolete for cryptographic security)

> ⚠️ **Note:** MD2 is considered cryptographically broken and should not be used for modern security purposes. Prefer stronger algorithms like SHA-256 or SHA-3.