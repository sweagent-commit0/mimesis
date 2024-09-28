"""This module provides internal util functions."""

def luhn_checksum(num: str) -> str:
    """Calculate a checksum for num using the Luhn algorithm.

    Used to validate credit card numbers, IMEI numbers,
    and other identification numbers.

    :param num: The number to calculate a checksum for as a string.
    :return: Checksum for number.
    """
    pass