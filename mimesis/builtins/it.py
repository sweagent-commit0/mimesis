"""Specific data provider for Italy (it)."""
import string
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed
__all__ = ['ItalySpecProvider']

class ItalySpecProvider(BaseDataProvider):
    """Specific-provider of misc data for Italy."""

    def __init__(self, seed: Seed=MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.IT, seed=seed)

    class Meta:
        name = 'italy_provider'
        datafile = 'builtin.json'

    def fiscal_code(self, gender: Gender | None=None) -> str:
        """Return a random fiscal code.

        :param gender: Gender's enum object.
        :return: Fiscal code.

        Example:
            RSSMRA66R05D612U
        """
        pass