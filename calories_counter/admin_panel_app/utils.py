import pandas as pd
from django.core.exceptions import ValidationError


class AdminPanelUtils:

    def __init__(self, file_extension: str = '.csv') -> None:
        self.file_extension = file_extension

    def validate_file_extension(self, csv_file) -> None:
        """
        This function is responsible for validating the file extension.
        :param csv_file:
        :return: None
        """
        if not csv_file.name.endswith(self.file_extension):
            raise ValidationError(f'Only {self.file_extension} file are allowed!')

        try:
            pd.read_csv(csv_file)
        except pd.errors.ParserError:
            raise ValidationError(f'Invalid {self.file_extension} file!')

