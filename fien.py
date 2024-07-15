from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a cryptographic key using the Fernet symmetric encryption algorithm.
    """
    return Fernet.generate_key()

def save_key(key, key_file):
    """
    Save a cryptographic key to a file.
    """
    with open(key_file, 'wb') as key_file:
        key_file.write(key)


def load_key(key_file):
    """
    Load a cryptographic key from a file.
    """
    with open(key_file, 'rb') as key_file:
        return key_file.read()

def encrypt_file(input_file, output_file, key):
    """
    Encrypt a file using the Fernet symmetric encryption algorithm.
    """
    with open(input_file, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(input_file, output_file, key):
    """
    Decrypt a file using the Fernet symmetric encryption algorithm.
    """
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)


if __name__ == '__main__':
    key = generate_key()
    key_file = 'encryption_key.key'
    save_key(key, key_file)

    input_file = 'plaintext.txt'
    encrypted_file = 'encrypted_file.txt'
    decrypted_file = 'decrypted_file.txt'

    encrypt_file(input_file, encrypted_file, key)
    print(f'Encrypted {input_file} as {encrypted_file}')

    decrypt_file(encrypted_file, decrypted_file, key)
    print(f'Decrypted {encrypted_file} as {decrypted_file}')