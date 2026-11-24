from cryptography.hazmat.primitives.asymmetric import dh, ec, x25519


def ecdh_secret(peer):
    key = ec.generate_private_key(ec.SECP256R1())
    return key.exchange(ec.ECDH(), peer)


def x25519_secret(peer):
    key = x25519.X25519PrivateKey.generate()
    return key.exchange(peer)


def ffdh_secret(peer):
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    key = parameters.generate_private_key()
    return key.exchange(peer)
