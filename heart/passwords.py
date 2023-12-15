import bcrypt


def hash_pass(passphrase):
    # Adding the salt to password
    salt = bcrypt.gensalt()

    # Hashing the password
    hashed = bcrypt.hashpw(passphrase, salt)

    return hashed


def verify_pass(entered_passphrase, stored_hashed_passphrase):
    # Encode the entered passphrase to bytes using UTF-8
    entered_passphrase_bytes = entered_passphrase.encode('utf-8')

    # Verify the password
    return bcrypt.checkpw(entered_passphrase_bytes, stored_hashed_passphrase)
