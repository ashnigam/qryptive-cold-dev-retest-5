from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding


def sign_invoice(invoice: bytes) -> bytes:
    rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    return rsa_key.sign(invoice, padding.PKCS1v15(), hashes.SHA256())


def sign_webhook(body: bytes) -> bytes:
    ec_key = ec.generate_private_key(ec.SECP256R1())
    return ec_key.sign(body, ec.ECDSA(hashes.SHA256()))
