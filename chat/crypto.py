import base64
import hashlib
from django.conf import settings
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def _derive_key() -> bytes:
    """Derive a 32-byte key from Django's SECRET_KEY using SHA-256."""
    return hashlib.sha256(settings.SECRET_KEY.encode()).digest()


def decrypt_message(encrypted_b64: str) -> str:
    """Decrypt a base64-encoded (nonce + ciphertext) string produced by AES-GCM.

    Returns the plaintext string, or an empty string if the input is empty or
    decryption fails.
    """
    if not encrypted_b64:
        return ''

    try:
        data = base64.b64decode(encrypted_b64)
        nonce = data[:12]
        ct = data[12:]
        key = _derive_key()
        aesgcm = AESGCM(key)
        pt = aesgcm.decrypt(nonce, ct, None)
        return pt.decode('utf-8')
    except Exception:
        # On any failure, return empty string to avoid exposing raw ciphertext
        # to templates. We could also raise or log depending on needs.
        return ''
