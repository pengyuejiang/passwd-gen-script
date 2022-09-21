import hashlib
import getpass

# Parameters for password generation
ORDER_OF_MAGNITUDE = 32
CHARSET_SIZE = 95
OFFSET = 32

seed = input('Password Generation Seed: ')
while True:
    meta_passwd = getpass.getpass('Meta-Password: ')
    meta_passwd_again = getpass.getpass('The same thing again: ')
    if meta_passwd == meta_passwd_again:
        break
    else:
        print('They don\'t match, try again.')
year = int(input('Year: '))

bytestr = bytes(seed + meta_passwd + str(year), 'utf-8')
decimal = int(hashlib.sha256(bytestr).hexdigest()[-ORDER_OF_MAGNITUDE:], 16)
passwd = []
while decimal > 0:
    current_num = decimal % CHARSET_SIZE
    decimal //= CHARSET_SIZE
    passwd.append(chr(OFFSET + current_num))
passwd.reverse()
print('Password:', ''.join(passwd))
print('Length:', len(passwd))
