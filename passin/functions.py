import hashlib
import os

LENGTH = 8
ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')

def gen_secretkey():
    """Generates a secret key and sets an enviroment variable to it.
    """

    key = os.urandom(24).encode('hex')
    os.environ['PASSINKEY'] = key

def get_hexdigest(salt, password):
    """Return a hashed version of the master password and service,
    
    Arguments:
        salt {str} -- The name of the service the password is for.
        password {str} -- The master password.
    
    Returns:
        str -- Hash of the salt and password, in hex.
    """

    return hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

def gen_password(plaintext, service):
    """Generates a password using the service name and master password.
    
    Arguments:
        plaintext {str} -- The master password.
        service {str} -- The service name.
    
    Returns:
        [str] -- A generated password.
    """

    secret_key = os.environ['PASSINKEY']
    salt = get_hexdigest(secret_key, service)
    hsh = get_hexdigest(salt, plaintext)
    return ''.join(salt + hsh)

