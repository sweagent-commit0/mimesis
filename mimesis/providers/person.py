"""Provides personal data."""
import hashlib
import re
import typing as t
import uuid
from datetime import date, datetime
from string import ascii_letters, digits, punctuation
from mimesis.datasets import BLOOD_GROUPS, CALLING_CODES, EMAIL_DOMAINS, GENDER_CODES, GENDER_SYMBOLS, USERNAMES
from mimesis.enums import Gender, TitleType
from mimesis.providers.base import BaseDataProvider
from mimesis.types import Date
__all__ = ['Person']

class Person(BaseDataProvider):
    """Class for generating personal data."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)

    class Meta:
        name = 'person'
        datafile = f'{name}.json'

    def birthdate(self, min_year: int=1980, max_year: int=2023) -> Date:
        """Generates a random birthdate as a :py:class:`datetime.date` object.

        :param min_year: Maximum birth year.
        :param max_year: Minimum birth year.
        :return: Random date object.
        """
        pass

    def name(self, gender: Gender | None=None) -> str:
        """Generates a random name.

        :param gender: Gender's enum object.
        :return: Name.

        :Example:
            John.
        """
        pass

    def first_name(self, gender: Gender | None=None) -> str:
        """Generates a random first name.

        ..note: An alias for :meth:`~.name`.

        :param gender: Gender's enum object.
        :return: First name.
        """
        pass

    def surname(self, gender: Gender | None=None) -> str:
        """Generates a random surname.

        :param gender: Gender's enum object.
        :return: Surname.

        :Example:
            Smith.
        """
        pass

    def last_name(self, gender: Gender | None=None) -> str:
        """Generates a random last name.

        ..note: An alias for :meth:`~.surname`.

        :param gender: Gender's enum object.
        :return: Last name.
        """
        pass

    def title(self, gender: Gender | None=None, title_type: TitleType | None=None) -> str:
        """Generates a random title for name.

        You can generate a random prefix or suffix
        for name using this method.

        :param gender: The gender.
        :param title_type: TitleType enum object.
        :return: The title.
        :raises NonEnumerableError: if gender or title_type in incorrect format.

        :Example:
            PhD.
        """
        pass

    def full_name(self, gender: Gender | None=None, reverse: bool=False) -> str:
        """Generates a random full name.

        :param reverse: Return reversed full name.
        :param gender: Gender's enum object.
        :return: Full name.

        :Example:
            Johann Wolfgang.
        """
        pass

    def username(self, mask: str | None=None, drange: tuple[int, int]=(1800, 2100)) -> str:
        """Generates a username by mask.

        Masks allow you to generate a variety of usernames.

        - **C** stands for capitalized username.
        - **U** stands for uppercase username.
        - **l** stands for lowercase username.
        - **d** stands for digits in the username.

        You can also use symbols to separate the different parts
        of the username: **.** **_** **-**

        :param mask: Mask.
        :param drange: Digits range.
        :raises ValueError: If template is not supported.
        :return: Username as string.

        Example:
            >>> username(mask='C_C_d')
            Cotte_Article_1923
            >>> username(mask='U.l.d')
            ELKINS.wolverine.2013
            >>> username(mask='l_l_d', drange=(1900, 2021))
            plasmic_blockader_1907
        """
        pass

    def password(self, length: int=8, hashed: bool=False) -> str:
        """Generates a password or hash of password.

        :param length: Length of password.
        :param hashed: SHA256 hash.
        :return: Password or hash of password.

        :Example:
            k6dv2odff9#4h
        """
        pass

    def email(self, domains: t.Sequence[str] | None=None, unique: bool=False) -> str:
        """Generates a random email.

        :param domains: List of custom domains for emails.
        :param unique: Makes email addresses unique.
        :return: Email address.
        :raises ValueError: if «unique» is True and the provider was seeded.

        :Example:
            foretime10@live.com
        """
        pass

    def gender_symbol(self) -> str:
        """Generate a random sex symbol.

        :Example:
            ♂
        """
        pass

    def gender_code(self) -> int:
        """Generate a random ISO/IEC 5218 gender code.

        Generate a random title of gender code for the representation
        of human sexes is an international standard that defines a
        representation of human sexes through a language-neutral single-digit
        code or symbol of gender.

        Codes for the representation of human sexes is an international
        standard (0 - not known, 1 - male, 2 - female, 9 - not applicable).

        :return:
        """
        pass

    def gender(self) -> str:
        """Generates a random gender title.

        :Example:
            Male
        """
        pass

    def sex(self) -> str:
        """An alias for method :meth:`~.gender`.

        :return: Sex.
        """
        pass

    def height(self, minimum: float=1.5, maximum: float=2.0) -> str:
        """Generates a random height in meters.

        :param minimum: Minimum value.
        :param float maximum: Maximum value.
        :return: Height.

        :Example:
            1.85.
        """
        pass

    def weight(self, minimum: int=38, maximum: int=90) -> int:
        """Generates a random weight in Kg.

        :param minimum: min value
        :param maximum: max value
        :return: Weight.

        :Example:
            48.
        """
        pass

    def blood_type(self) -> str:
        """Generates a random blood type.

        :return: Blood type (blood group).

        :Example:
            A+
        """
        pass

    def occupation(self) -> str:
        """Generates a random job.

        :return: The name of job.

        :Example:
            Programmer.
        """
        pass

    def political_views(self) -> str:
        """Get a random political views.

        :return: Political views.

        :Example:
            Liberal.
        """
        pass

    def worldview(self) -> str:
        """Generates a random worldview.

        :return: Worldview.

        :Example:
            Pantheism.
        """
        pass

    def views_on(self) -> str:
        """Get a random views on.

        :return: Views on.

        :Example:
            Negative.
        """
        pass

    def nationality(self, gender: Gender | None=None) -> str:
        """Generates a random nationality.

        :param gender: Gender.
        :return: Nationality.

        :Example:
            Russian
        """
        pass

    def university(self) -> str:
        """Generates a random university name.

        :return: University name.

        :Example:
            MIT.
        """
        pass

    def academic_degree(self) -> str:
        """Generates a random academic degree.

        :return: Degree.

        :Example:
            Bachelor.
        """
        pass

    def language(self) -> str:
        """Generates a random language name.

        :return: Random language.

        :Example:
            Irish.
        """
        pass

    def phone_number(self, mask: str='', placeholder: str='#') -> str:
        """Generates a random phone number.

        :param mask: Mask for formatting number.
        :param placeholder: A placeholder for a mask (default is #).
        :return: Phone number.

        :Example:
            +7-(963)-409-11-22.
        """
        pass

    def telephone(self, *args: t.Any, **kwargs: t.Any) -> str:
        """An alias for :meth:`~.phone_number`."""
        pass

    def identifier(self, mask: str='##-##/##') -> str:
        """Generates a random identifier by mask.

        With this method, you can generate any identifiers that
        you need by specifying the mask.

        :param mask:
            The mask. Here ``@`` is a placeholder for characters and ``#`` is
            placeholder for digits.
        :return: An identifier.

        :Example:
            07-97/04
        """
        pass