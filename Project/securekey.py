from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import base64

# Function to generate a random encryption key
def generate_encryption_key(password):
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    print(key)
    return key

# Function to encrypt the secret key
def encrypt_secret_key(secret_key, encryption_key):
    cipher = AES.new(encryption_key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(secret_key.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    encrypted_data = base64.b64encode(ciphertext).decode('utf-8')
    return iv, encrypted_data

# Function to decrypt the secret key
def decrypt_secret_key(encrypted_data, iv, encryption_key):
    cipher = AES.new(encryption_key, AES.MODE_CBC, base64.b64decode(iv))
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)
    return decrypted_data.decode('utf-8')

