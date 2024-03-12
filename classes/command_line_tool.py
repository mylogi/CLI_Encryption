import argparse

from classes.file_manager import FileManager
from classes.data_encryptor import DataEncryptor
from classes.data_decryptor import DataDecryptor


class CommandLineTool:
    """A CommandLineTool class contains the main logic of CLI instrument.

    Additional details about the class can be added here if needed.
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="A simple CLI tool.")
        self._configure_arguments()
        self.file_manager = FileManager()
        self.input_text: str = ""

    def _configure_arguments(self) -> None:
        self.parser.add_argument('--encrypt', help='File path for Encryption')
        self.parser.add_argument('--decrypt', help='File path for Decryption')

    def _process_arguments(self, args) -> tuple | None:

        if args.encrypt is not None:

            print(f"File path for Encryption: {args.encrypt}")

            if self.file_manager.check_file(args.encrypt):

                return True, args.encrypt
            else:
                print("File doesn't exist")
        elif args.decrypt is not None:

            print(f"File path for Decryption: {args.decrypt}")

            if self.file_manager.check_file(args.decrypt):

                return False, args.decrypt
            else:
                print("File doesn't exist")

                return None, None
        else:
            print("No option specified")

    def _encrypt_data(self, state_tuple: tuple) -> str:

        data_encryptor = DataEncryptor(
            key=self.file_manager.return_content(state_tuple[1]),
            nonce=self.file_manager.return_content(self.file_manager.nonce_path)
        )

        return data_encryptor.encrypt_data(self.file_manager.encode_string(self.input_text)).hex()

    def _decrypt_data(self, state_tuple: tuple) -> bytes:

        data_decryptor = DataDecryptor(
            key=self.file_manager.return_content(state_tuple[1]),
            nonce=self.file_manager.return_content(self.file_manager.nonce_path)
        )

        return data_decryptor.decrypt_data(bytes.fromhex(self.input_text))

    def encrypt_or_decrypt(self, state_tuple: tuple) -> None | bytes | str:
        if state_tuple[0] is None:
            print("Not today")
        elif state_tuple[0] is True:
            return self._encrypt_data(state_tuple=state_tuple)
        elif state_tuple[0] is False:
            return self._decrypt_data(state_tuple=state_tuple)

    def input_loop(self) -> None:

        while True:
            input_text = input("Please enter your text: ")
            if len(input_text) > 0:
                self.input_text = input_text
                break
            else:
                continue

    def run(self) -> tuple | None:
        args = self.parser.parse_args()
        path_arg = self._process_arguments(args)
        return path_arg
