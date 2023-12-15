from argon2 import PasswordHasher


def hash_pass(passphrase):
    ph = PasswordHasher()
    return ph.hash(passphrase)

def verify_pass(stored_pass, input_pass):
    ph = PasswordHasher()
    return ph.verify(stored_pass, input_pass)
