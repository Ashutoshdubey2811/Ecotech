import sys
from src.Ecotech_project.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.error_message_detail(error_message, error_detail)

    @staticmethod
    def error_message_detail(error_message, error_detail: sys) -> str:
        """Return a detailed error message with file name and line number."""
        _, _, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        detailed_message = (
            f"Error occurred in script: {file_name} "
            f"at line number: {line_number} "
            f"with message: {error_message}"
        )
        return detailed_message

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return f"{self.__class__.__name__}({self.error_message})"
