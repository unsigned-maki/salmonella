import hashlib


def hash_str(string):
    return hashlib.sha256(string.encode()).digest()
