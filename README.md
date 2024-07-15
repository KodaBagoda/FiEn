## Secure File Encryption with Fernet (Python)

This Python project provides a basic file encryption and decryption tool using the Fernet library, offering a layer of security for your sensitive data.

**Features:**

- Encrypts and decrypts files using the Fernet symmetric encryption algorithm.
- Generates a secure key for encryption and saves it to a separate file (`encryption_key.key`).
- Encrypts and decrypts files specified by their paths.
- Provides user-friendly output messages to indicate success.

**Dependencies:**

- This project requires the `cryptography` library. Install it using `pip install cryptography`.

**Important Warning:**

- **Securing the Key File is Crucial:** The security of your encrypted files relies heavily on the protection of the key file (`encryption_key.key`).
  - Store the key file in a secure location, ideally outside of the directory containing your encrypted files.
  - Consider using a password manager for additional protection of the key.
- **Fernet is for Single-Use Encryption:** While Fernet offers encryption, it's not ideal for password management or other scenarios where multiple users need to decrypt files. Explore dedicated password managers or other encryption solutions for those use cases.

**Usage:**

1. Clone this repository.
2. Open a terminal and navigate to the project directory.
3. Run the script (`file_encryption.py`) using `python file_encryption.py`.
   - The script will automatically generate a key, save it to `encryption_key.key`, encrypt your sample file (`plaintext.txt`), and decrypt the encrypted version (`encrypted_file.txt`).
4. **To encrypt a different file:**
   - Edit the `input_file` variable in the script to point to the file you want to encrypt.
   - Run the script again.

**Example Output:**

```
Encrypted plaintext.txt as encrypted_file.txt
Decrypted encrypted_file.txt as decrypted_file.txt
```

**Disclaimer:**

This script is intended for demonstration purposes and learning about file encryption. **For real-world use:**

- Securely store the key file.
- Consider using a more robust encryption solution with key management features for sensitive data.

**Contributing:**

Feel free to fork this repository and make improvements! Here are some ideas:

- Implement user input for file paths instead of using predefined examples.
- Allow users to specify a custom key file name.
- Add error handling for invalid file paths or key file issues.

**Security Considerations:**

- Remember, the key file is critical for decrypting your files. Take appropriate measures to safeguard it.
- Explore more advanced encryption solutions with stronger key management practices for enhanced security in production environments.
