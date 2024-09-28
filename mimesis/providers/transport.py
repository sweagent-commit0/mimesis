"""Provides data related to transports."""
from mimesis.datasets import AIRPLANES, AUTO_MANUFACTURERS, CARS, VR_CODES, VRC_BY_LOCALES
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
__all__ = ['Transport']

class Transport(BaseProvider):
    """Class for generating data related to transports."""

    class Meta:
        name = 'transport'

    def manufacturer(self) -> str:
        """Generates a random car manufacturer.

        :return: A car manufacturer

        :Example:
            Tesla.
        """
        pass

    def car(self) -> str:
        """Generates a random vehicle name.

        :return: A vehicle.

        :Example:
            Tesla Model S.
        """
        pass

    def airplane(self) -> str:
        """Generates a random airplane model name.

        :return: Airplane model.

        :Example:
            Boeing 727.
        """
        pass

    def vehicle_registration_code(self, locale: Locale | None=None) -> str:
        """Returns vehicle registration code.

        :param locale: Registration code for locale (country).
        :return: Vehicle registration code.
        """
        pass