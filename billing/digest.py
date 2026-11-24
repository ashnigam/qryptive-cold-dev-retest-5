import hashlib


def cache_key(body: bytes) -> str:
    return hashlib.md5(body).hexdigest()


def legacy_row_id(body: bytes) -> str:
    return hashlib.sha1(body).hexdigest()
