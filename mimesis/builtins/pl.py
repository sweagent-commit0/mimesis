"""Specific data provider for Poland (pl)."""
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider, Datetime
from mimesis.types import DateTime, MissingSeed, Seed
__all__ = ['PolandSpecProvider']

class PolandSpecProvider(BaseDataProvider):
    """Class that provides special data for Poland (pl)."""

    def __init__(self, seed: Seed=MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.PL, seed=seed)

    class Meta:
        name = 'poland_provider'
        datafile = None

    def nip(self) -> str:
        """Generate random valid 10-digit NIP.

        :return: Valid 10-digit NIP
        """
        pass

    def pesel(self, birth_date: DateTime | None=None, gender: Gender | None=None) -> str:
        """Generate random 11-digit PESEL.

        :param birth_date: Initial birthdate (optional)
        :param gender: Gender of the person.
        :return: Valid 11-digit PESEL
        """
        pass

    def regon(self) -> str:
        """Generate random valid 9-digit REGON.

        :return: Valid 9-digit REGON
        """
        pass