import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class Vault:
    def session_key(self) -> bytes:
        return AESGCM.generate_key(bit_length=128)

    def master_key(self) -> bytes:
        return AESGCM.generate_key(bit_length=256)

    def seal(self, key: bytes, data: bytes) -> bytes:
        return AESGCM(key).encrypt(os.urandom(12), data, None)
