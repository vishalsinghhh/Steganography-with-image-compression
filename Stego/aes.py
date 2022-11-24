from Crypto.Cipher import AES

password = input()
key = bytes(password, 'utf-8')

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

password1 = input()
key1 = bytes(password1, 'utf-8')
def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key1, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)
if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')