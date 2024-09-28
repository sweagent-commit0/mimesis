"""Address module.

This module contains provider Address() and other utils which represent
data related to location, such as street name, city etc.
"""
import typing as t
from mimesis.datasets import CALLING_CODES, CONTINENT_CODES, COUNTRY_CODES, SHORTENED_ADDRESS_FMT
from mimesis.enums import CountryCode
from mimesis.providers.base import BaseDataProvider
__all__ = ['Address']

class Address(BaseDataProvider):
    """Class for generate fake address data.

    This object provides all the data related to
    geographical location.
    """

    class Meta:
        name = 'address'
        datafile = f'{name}.json'

    @staticmethod
    def _dd_to_dms(num: float, _type: str) -> str:
        """Converts decimal number to DMS format.

        :param num: Decimal number.
        :param _type: Type of number.
        :return: Number in DMS format.
        """
        pass

    def street_number(self, maximum: int=1400) -> str:
        """Generates a random street number.

        :param maximum: Maximum value.
        :return: Street number.
        """
        pass

    def street_name(self) -> str:
        """Generates a random street name.

        :return: Street name.
        """
        pass

    def street_suffix(self) -> str:
        """Generates a random street suffix.

        :return: Street suffix.
        """
        pass

    def address(self) -> str:
        """Generates a random full address.

        :return: Full address.
        """
        pass

    def state(self, abbr: bool=False) -> str:
        """Generates a random administrative district of the country.

        :param abbr: Return ISO 3166-2 code.
        :return: Administrative district.
        """
        pass

    def region(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random region.

        An alias for :meth:`~.state()`.
        """
        pass

    def province(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random province.

        An alias for :meth:`~.state()`.
        """
        pass

    def federal_subject(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random federal_subject (Russia).

        An alias for :meth:`~.state()`.
        """
        pass

    def prefecture(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random prefecture.

        An alias for :meth:`~.state()`.
        """
        pass

    def postal_code(self) -> str:
        """Generates a postal code for current locale.

        :return: Postal code.
        """
        pass

    def zip_code(self) -> str:
        """Generates a zip code.

        An alias for :meth:`~.postal_code()`.

        :return: Zip code.
        """
        pass

    def country_code(self, code: CountryCode | None=CountryCode.A2) -> str:
        """Generates a random code of country.

        Default format is :attr:`~enums.CountryCode.A2` (ISO 3166-1-alpha2),
        you can change it by passing parameter ``fmt``.

        :param code: Country code.
        :return: Country code in selected format.
        :raises KeyError: if fmt is not supported.
        """
        pass

    def country_emoji_flag(self) -> str:
        """Generates a randomly chosen country emoji flag.

        :example:
            🇹🇷

        :return: Flag emoji.
        """
        pass

    def default_country(self) -> str:
        """Returns the country associated with the current locale.

        :return: The country associated with current locale.
        """
        pass

    def country(self) -> str:
        """Generates a random country.

        :return: The Country.
        """
        pass

    def city(self) -> str:
        """Generates a random city.

        :return: City name.
        """
        pass

    def _get_fs(self, key: str, dms: bool=False) -> str | float:
        """Get float number.

        :param key: Key (`lt` or `lg`).
        :param dms: DMS format.
        :return: Float number
        """
        pass

    def latitude(self, dms: bool=False) -> str | float:
        """Generates a random value of latitude.

        :param dms: DMS format.
        :return: Value of longitude.
        """
        pass

    def longitude(self, dms: bool=False) -> str | float:
        """Generates a random value of longitude.

        :param dms: DMS format.
        :return: Value of longitude.
        """
        pass

    def coordinates(self, dms: bool=False) -> dict[str, str | float]:
        """Generates random geo coordinates.

        :param dms: DMS format.
        :return: Dict with coordinates.
        """
        pass

    def continent(self, code: bool=False) -> str:
        """Returns a random continent name or continent code.

        :param code: Return code of a continent.
        :return: Continent name.
        """
        pass

    def calling_code(self) -> str:
        """Generates a random calling code of random country.

        :return: Calling code.
        """
        pass

    def isd_code(self) -> str:
        """Generates a random ISD code.

        An alias for :meth:`~Address.calling_code()`.
        """
        pass