from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def get_hash_user_password(user_password):
    return password_hash.hash(user_password)


def verify_password(current_password, user_password_hash):
    return password_hash.verify(current_password, user_password_hash)
