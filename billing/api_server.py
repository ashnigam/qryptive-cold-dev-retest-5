import ssl
from cryptography.hazmat.primitives.asymmetric import ed25519


def tls_server() -> ssl.SSLContext:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.load_cert_chain(certfile="tls/api.pem", keyfile="tls/api.key")
    return ctx


def sign_receipt(receipt: bytes) -> bytes:
    receipt_key = ed25519.Ed25519PrivateKey.generate()
    return receipt_key.sign(receipt)
