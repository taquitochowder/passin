import hashlib
import os
import secrets

LENGTH = 8
ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')


def key_exists():
    return 'PASSINKEY' in os.environ


def gen_secretkey():
    """Generates a secret key and sets it.
    """

    key = secrets.token_hex(16)
    set_secretkey(key)


def set_secretkey(key):
    """Sets an environment variable to the key.

    Arguments:
        key {str} -- The secret key.
    """

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
    """Generates a password in hex using the service name and master password.

    Arguments:
        plaintext {str} -- The master password.
        service {str} -- The service name.

    Returns:
        [str] -- A generated password.
    """

    secret_key = os.environ['PASSINKEY']
    salt = get_hexdigest(secret_key, service)
    hsh = get_hexdigest(salt, plaintext)
    return salt + hsh


def password(plaintext, service, length=LENGTH, alphabet=ALPHABET):
    """Creates a usable password based on certain parameters.

    Arguments:
        plaintext {str} -- The master password.
        service {str} -- The service name.

    Keyword Arguments:
        length {int} -- The length of the password. (default: {LENGTH})
        alphabet {str} -- The letters that the password can be made of. (default: {ALPHABET})

    Returns:
        [str] -- The password corresponding to the service.
    """

    # 16 is needed is specify that it is hex
    num = int(gen_password(plaintext, service), 16)

    # Used as the base that num will be converted to, base-74 by default
    num_chars = len(alphabet)

    chars = []
    while len(chars) < length:
        num, rem = divmod(num, num_chars)
        chars.append(alphabet[rem])

    return ''.join(chars)
