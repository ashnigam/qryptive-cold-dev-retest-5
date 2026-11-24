from Crypto.Cipher import DES, ARC4, Blowfish


def encrypt_export(key: bytes, blob: bytes) -> bytes:
    return DES.new(key, DES.MODE_CBC, iv=b"\x00" * 8).encrypt(blob)


def stream_obfuscate(key: bytes, blob: bytes) -> bytes:
    return ARC4.new(key).encrypt(blob)


def archive_encrypt(key: bytes, blob: bytes) -> bytes:
    return Blowfish.new(key, Blowfish.MODE_ECB).encrypt(blob)
