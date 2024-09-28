"""File data provider."""
from mimesis.datasets import EXTENSIONS, FILENAMES, MIME_TYPES
from mimesis.enums import FileType, MimeType
from mimesis.providers.base import BaseProvider
__all__ = ['File']

class File(BaseProvider):
    """Class for generate data related to files."""

    class Meta:
        name = 'file'

    def extension(self, file_type: FileType | None=None) -> str:
        """Generates a random file extension.

        :param file_type: Enum object FileType.
        :return: Extension of the file.

        :Example:
            .py
        """
        pass

    def mime_type(self, type_: MimeType | None=None) -> str:
        """Generates a random mime type.

        :param type_: Enum object MimeType.
        :return: Mime type.
        """
        pass

    def size(self, minimum: int=1, maximum: int=100) -> str:
        """Generates a random file size as string.

        :param minimum: Maximum value.
        :param maximum: Minimum value.
        :return: Size of file.

        :Example:
            56 kB
        """
        pass

    def file_name(self, file_type: FileType | None=None) -> str:
        """Generates a random file name with an extension.

        :param file_type: Enum object FileType
        :return: File name.

        :Example:
            legislative.txt
        """
        pass