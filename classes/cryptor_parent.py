import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class CryptorParent:
    """A CryptorParent class contains the shared logic for DataEncryptor and DataDecryptor.

    Additional details about the class can be added here if needed.
    """

    def __init__(
            self,
            key: bytes = b"",
            nonce: bytes = b"",
            associated_data: bytes = b"authenticated but unencrypted data"
    ):
        self.random_constant: int = 12
        self.cipher = AESGCM
        self.key: bytes = self.add_key(key)
        self.nonce: bytes = nonce
        self.associated_data: bytes = associated_data

    def _return_nonce(self) -> bytes:
        nonce = os.urandom(self.random_constant)

        return nonce

    def _return_aesgcm(self):
        aesgcm = self.cipher(self.key)

        return aesgcm

    def get_nonce(self) -> bytes:
        if self.nonce == b"":
            self.nonce = self._return_nonce()
            return self.nonce
        else:
            return self.nonce

    def generate_key(self, bit_length=256) -> bytes:
        return self.cipher.generate_key(bit_length)

    def add_key(self, key: bytes = None):
        if key == b"":
            return self.generate_key()
        else:
            return key
