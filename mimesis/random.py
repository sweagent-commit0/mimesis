"""Implements various helpers which are used in the various data providers.

This module contains custom ``Random()`` class where implemented a lot of
methods which are not included in standard :py:class:`random.Random`,
but frequently used in this project.
"""
import random as random_module
import typing as t
from mimesis.types import MissingSeed, Seed
__all__ = ['Random', 'random']
global_seed: Seed = MissingSeed

class Random(random_module.Random):
    """A custom random class.

    It is a subclass of the :py:class:`random.Random` class from the standard
    library's random module. The class incorporates additional custom methods.

    This class can be extended according to specific requirements.
    """

    def randints(self, n: int=3, a: int=1, b: int=100) -> list[int]:
        """Generate a list of random integers.

        :param n: Number of elements.
        :param a: Minimum value of range.
        :param b: Maximum value of range.
        :return: List of random integers.
        :raises ValueError: if the number is less or equal to zero.
        """
        pass

    def _generate_string(self, str_seq: str, length: int=10) -> str:
        """Generate random string created from a string sequence.

        :param str_seq: String sequence of letters or digits.
        :param length: Max value.
        :return: Single string.
        """
        pass

    def generate_string_by_mask(self, mask: str='@###', char: str='@', digit: str='#') -> str:
        """Generate custom code using ascii uppercase and random integers.

        :param mask: Mask of code.
        :param char: Placeholder for characters.
        :param digit: Placeholder for digits.
        :return: Custom code.
        """
        pass

    def uniform(self, a: float, b: float, precision: int=15) -> float:
        """Get a random number in the range [a, b) or [a, b] depending on rounding.

        :param a: Minimum value.
        :param b: Maximum value.
        :param precision: Round a number to a given
            precision in decimal digits, default is 15.
        """
        pass

    def randbytes(self, n: int=16) -> bytes:
        """Generate n random bytes."""
        pass

    def weighted_choice(self, choices: dict[t.Any, float]) -> t.Any:
        """Returns a random element according to the specified weights.

        :param choices: A dictionary where keys are choices and values are weights.
        :raises ValueError: If choices are empty.
        :return: Random key from dictionary.
        """
        pass

    def choice_enum_item(self, enum: t.Any) -> t.Any:
        """Get random value of enum object.

        :param enum: Enum object.
        :return: Random value of enum.
        """
        pass
random = Random()