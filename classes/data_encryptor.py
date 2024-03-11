from classes.cryptor_parent import CryptorParent


class DataEncryptor(CryptorParent):

    def __init__(
            self,
            key: bytes = b"",
            nonce: bytes = b"",
            associated_data: bytes = b"authenticated but unencrypted data"
    ):
        super().__init__(
            key=key,
            nonce=nonce,
            associated_data=associated_data
        )

    def encrypt_data(self, data: bytes):
        encryption_data = self._return_aesgcm().encrypt(
            nonce=self.nonce,
            data=data,
            associated_data=self.associated_data
        )

        return encryption_data
