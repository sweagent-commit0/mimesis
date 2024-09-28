"""Specific data provider for Russia (ru)."""
from datetime import datetime
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed
__all__ = ['RussiaSpecProvider']

class RussiaSpecProvider(BaseDataProvider):
    """Class that provides special data for Russia (ru)."""

    def __init__(self, seed: Seed=MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.RU, seed=seed)
        self._current_year = str(datetime.now().year)

    class Meta:
        """The name of the provider."""
        name = 'russia_provider'
        datafile = 'builtin.json'

    def generate_sentence(self) -> str:
        """Generate sentence from the parts.

        :return: Sentence.
        """
        pass

    def patronymic(self, gender: Gender | None=None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.

        :Example:
            Алексеевна.
        """
        pass

    def passport_series(self, year: int | None=None) -> str:
        """Generate random series of passport.

        :param year: Year of manufacture.
        :type year: int or None
        :return: Series.

        :Example:
            02 15.
        """
        pass

    def passport_number(self) -> int:
        """Generate random passport number.

        :return: Number.

        :Example:
            560430
        """
        pass

    def series_and_number(self) -> str:
        """Generate a random passport number and series.

        :return: Series and number.

        :Example:
            57 16 805199.
        """
        pass

    def snils(self) -> str:
        """Generate snils with a special algorithm.

        :return: SNILS.

        :Example:
            41917492600.
        """
        pass

    def inn(self) -> str:
        """Generate random, but valid ``INN``.

        :return: INN.
        """
        pass

    def ogrn(self) -> str:
        """Generate random valid ``OGRN``.

        :return: OGRN.

        :Example:
            4715113303725.
        """
        pass

    def bic(self) -> str:
        """Generate random ``BIC`` (Bank ID Code).

        :return: BIC.

        :Example:
            044025575.
        """
        pass

    def kpp(self) -> str:
        """Generate random ``KPP``.

        :return: 'KPP'.

        :Example:
            560058652.
        """
        pass