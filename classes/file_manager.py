import datetime
import os


class FileManager:
    """A FileManager class contains the main logic of file processing.

    Additional details about the class can be added here if needed.
    """

    def __init__(self, nonce_path: str = "/your/nonce/path/nonce.bin"):
        self.nonce_path = nonce_path
        self.file_path = f"./key{datetime.datetime.now()}.bin"
        self.utf_standard = 'utf-8'

    @staticmethod
    def return_content(path):
        with open(path, "rb") as bin_file:
            return bin_file.read()

    def encode_string(self, string: str) -> bytes:
        return string.encode(self.utf_standard)

    def save_content(self, data: str):
        with open(self.file_path, "wb") as bin_file:
            bin_file.write(self.encode_string(data))

    @staticmethod
    def check_file(path: str) -> bool:
        return os.path.exists(path)
