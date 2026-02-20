from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from django.conf import settings
import base64
import os

# Field-level encryption utility using AES-GCM
# Design choices:
# - Use AES-GCM for authenticated encryption (integrity + confidentiality).
# - The key is loaded from environment (settings.FIELD_ENCRYPTION_KEY) and must be 32 bytes (256 bits).
# - Each encryption produces: nonce (12 bytes) + ciphertext. Stored as raw bytes in BinaryField.
# - Decryption is intentionally not exposed via serializers or views. Only services should decrypt when necessary.

if not hasattr(settings, 'FIELD_ENCRYPTION_KEY'):
    # In dev it's acceptable to derive a key from SECRET_KEY but production MUST set a strong key via env.
    derived = (settings.SECRET_KEY * 2).encode()[:32]
    FIELD_ENCRYPTION_KEY = derived
else:
    FIELD_ENCRYPTION_KEY = base64.b64decode(settings.FIELD_ENCRYPTION_KEY)


def encrypt_field(plaintext: str) -> bytes:
    """Encrypts and returns raw bytes containing nonce + ciphertext.

    Args:
        plaintext: string to encrypt (utf-8)
    Returns:
        bytes: nonce + ciphertext
    """
    if plaintext is None:
        return None
    if isinstance(plaintext, str):
        plaintext_bytes = plaintext.encode('utf-8')
    else:
        plaintext_bytes = plaintext
    aesgcm = AESGCM(FIELD_ENCRYPTION_KEY)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, plaintext_bytes, associated_data=None)
    return nonce + ct


def decrypt_field(blob: bytes) -> str:
    """Decrypt bytes produced by encrypt_field. Returns plaintext string.

    WARNING: Use inside services only and never return raw decrypted value in APIs. APIs should only return masked values.
    """
    if blob is None:
        return None
    nonce = blob[:12]
    ct = blob[12:]
    aesgcm = AESGCM(FIELD_ENCRYPTION_KEY)
    pt = aesgcm.decrypt(nonce, ct, associated_data=None)
    return pt.decode('utf-8')

