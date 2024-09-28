"""Specific data provider for the Netherlands (nl)."""
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed
__all__ = ['NetherlandsSpecProvider']

class NetherlandsSpecProvider(BaseDataProvider):
    """Class that provides special data for the Netherlands (nl)."""

    def __init__(self, seed: Seed=MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.NL, seed=seed)

    class Meta:
        name = 'netherlands_provider'
        datafile = None

    def bsn(self) -> str:
        """Generate a random, but valid ``Burgerservicenummer``.

        :returns: Random BSN.

        :Example:
            255159705
        """
        pass

    def burgerservicenummer(self) -> str:
        """Generate a random, but valid ``Burgerservicenummer``.

        An alias for self.bsn()
        """
        pass