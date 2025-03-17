from Crypto.Cipher import DES
from secrets import token_bytes

key=token_bytes(8)
print(f"Key is :{key}")

def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce,ciphertext,tag):
    cipher=DES.new(key, DES.MODE_EAX , nonce=nonce)
    plaintext=cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode("ascii")
    except:
        return False

msg=input("Enter a Message:")
nonce,ciphertext,tag=encrypt(msg)

print(f"Ciphertext is :{ciphertext}")

plaintext=decrypt(nonce,ciphertext,tag)
if not plaintext:
    print("Message is Corrupted")
else :
          print(f"Plaintext is :{plaintext}")
   


