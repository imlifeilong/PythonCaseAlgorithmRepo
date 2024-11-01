import hashlib
import time


def get_token(user):
    """
    生成token
    """
    salt = str(time.time()).encode()
    m = hashlib.md5(user.encode())
    m.update(salt)
    return m.hexdigest()
