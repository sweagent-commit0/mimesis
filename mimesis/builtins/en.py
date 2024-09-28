"""Specific data provider for the USA (en)."""
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed
__all__ = ['USASpecProvider']

class USASpecProvider(BaseDataProvider):
    """Class that provides special data for the USA (en)."""

    def __init__(self, seed: Seed=MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.EN, seed=seed)

    class Meta:
        name = 'usa_provider'
        datafile = None

    def tracking_number(self, service: str='usps') -> str:
        """Generate random tracking number.

        Supported services: USPS, FedEx and UPS.

        :param str service: Post service.
        :return: Tracking number.
        """
        pass

    def ssn(self) -> str:
        """Generate a random, but valid SSN.

        :returns: SSN.

        :Example:
            569-66-5801
        """
        pass