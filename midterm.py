from cryptography.fernet import Fernet
import hashlib

type = input('Please enter input type\n1: string\n2: file\n')
usrInput = ''

if type == '1':
    usrInput = input('Enter string: ')
elif type == '2':
    file = open(input('File path: '), 'r')
    usrInput = file.read()
else:
    print('Error')

encodedInput = usrInput.encode()
hashedInput = hashlib.sha256(encodedInput).hexdigest()

key = Fernet.generate_key()
f = Fernet(key)
encryptedInput = f.encrypt(usrInput.encode())
decryptedInput = f.decrypt(encryptedInput).decode()

hashedDecrypted = hashlib.sha256(decryptedInput.encode()).hexdigest()

if hashedInput == hashedDecrypted:
    print('Hash comparison successful. File/string integrity preserved.')
    print(decryptedInput)
else:
    print('Hash comparison unsuccesful. File/string integrity not guaranteed.')