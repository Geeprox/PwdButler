import hashlib


def transform_key(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    m = m.hexdigest()
    return m[8:24]
