import datetime
import os
from typing import AnyStr


class FileManager:
    """A FileManager class contains the main logic of file processing.

    Additional details about the class can be added here if needed.
    """

    def __init__(
            self,
            nonce_path: str = "./binary_files/nonce.bin"
    ):
        self.nonce_path = nonce_path
        self.file_path = f"./key{datetime.datetime.now()}.bin"
        self.utf_standard = 'utf-8'

    def encode_string(self, string: str) -> bytes:
        return string.encode(self.utf_standard)

    def save_content(self, data: str) -> None:
        with open(self.file_path, "wb") as bin_file:
            bin_file.write(self.encode_string(data))

    @staticmethod
    def return_content(path) -> AnyStr:
        with open(path, "rb") as bin_file:
            return bin_file.read()

    @staticmethod
    def check_file(path: str) -> bool:
        return os.path.exists(path)
