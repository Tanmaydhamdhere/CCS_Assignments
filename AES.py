from Crypto.Cipher import AES
from secrets import token_bytes

key=token_bytes(16)
print(f"key is :{key}")

cipher=AES.new(key, AES.MODE_EAX)
data="My name is Shivam".encode()
nonce=cipher.nonce
ciphertext=cipher.encrypt(data)
print(f"Ciphertext is :{ciphertext}")
cipher=AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext=cipher.decrypt(ciphertext)
print(f"Plaintext is :{plaintext}")