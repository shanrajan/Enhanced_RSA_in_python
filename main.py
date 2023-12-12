import random
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

class KeyPair:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    p = getPrime(128)
    q = getPrime(128)
    r = getPrime(128)
    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)
    e = random.randrange(2, phi)
    while gcd(phi, e) != 1:
        e = random.randrange(2, phi)
    d = pow(e, -1, phi)
    return KeyPair(n, e, d)

def encrypt(n, e, message):
    return pow(bytes_to_long(message.encode()), e, n)

def decrypt(n, d, encrypted):
    return long_to_bytes(pow(encrypted, d, n)).decode()

if __name__ == "__main__":
    try:
        print("Generating Keys...")
        kp = generate_keys()
        print(f"Public Key: ({kp.n}, {kp.e})")
        print(f"Private Key: ({kp.n}, {kp.d})")
        print("\nTesting Encryption and Decryption...")
        message = input("Enter the Text to Encrypt: ")
        print(f"Original Message: {message}")
        encrypted = encrypt(kp.n, kp.e, message)
        print(f"Encrypted Message: {encrypted}")
        decrypted = decrypt(kp.n, kp.d, encrypted)
        print(f"Decrypted Message: {decrypted}")
    except Exception as e:
        print(f"Error: {e}")
