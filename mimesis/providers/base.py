"""Base data provider."""
import contextlib
import json
import operator
import typing as t
from functools import reduce
from mimesis import random as _random
from mimesis.constants import DATADIR, LOCALE_SEP
from mimesis.exceptions import NonEnumerableError
from mimesis.locales import Locale, validate_locale
from mimesis.types import JSON, MissingSeed, Seed
__all__ = ['BaseDataProvider', 'BaseProvider']

class BaseProvider:
    """This is a base class for all providers.


    :attr: random: An instance of :class:`mimesis.random.Random`.
    :attr: seed: Seed for random.
    """

    class Meta:
        name: str

    def __init__(self, *, seed: Seed=MissingSeed, random: _random.Random | None=None) -> None:
        """Initialize attributes.

        Keep in mind that locale-independent data providers will work
        only with keyword-only arguments.

        :param seed: Seed for random.
            When set to `None` the current system time is used.
        :param random: Custom random.
            See https://github.com/lk-geimfari/mimesis/issues/1313 for details.
        """
        if random is not None:
            if not isinstance(random, _random.Random):
                raise TypeError('The random must be an instance of mimesis.random.Random')
            self.random = random
        else:
            self.random = _random.Random()
        self.seed = seed
        self.reseed(seed)

    def reseed(self, seed: Seed=MissingSeed) -> None:
        """Reseeds the internal random generator.

        In case we use the default seed, we need to create a per instance
        random generator. In this case, two providers with the same seed
        will always return the same values.

        :param seed: Seed for random.
            When set to `None` the current system time is used.
        """
        pass

    def validate_enum(self, item: t.Any, enum: t.Any) -> t.Any:
        """Validates various enum objects that are used as arguments for methods.

        :param item: Item of an enum object.
        :param enum: Enum object.
        :return: Value of item.
        :raises NonEnumerableError: If enums has not such an item.
        """
        pass

    def _read_global_file(self, file_name: str) -> t.Any:
        """Reads JSON file and return dict.

        Reads JSON file from mimesis/data/global/ directory.

        :param file_name: Path to file.
        :raises FileNotFoundError: If the file was not found.
        :return: JSON data.
        """
        pass

    def _has_seed(self) -> bool:
        """Internal API to check if seed is set."""
        pass

    def __str__(self) -> str:
        """Human-readable representation of locale."""
        return self.__class__.__name__

class BaseDataProvider(BaseProvider):
    """This is a base class for all data providers."""

    def __init__(self, locale: Locale=Locale.DEFAULT, seed: Seed=MissingSeed, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes for data providers.

        :param locale: Current locale.
        :param seed: Seed to all the random functions.
        """
        super().__init__(*args, seed=seed, **kwargs)
        self._dataset: JSON = {}
        self._setup_locale(locale)
        self._load_dataset()

    def _setup_locale(self, locale: Locale=Locale.DEFAULT) -> None:
        """Set up locale after pre-check.

        :param str locale: Locale
        :raises UnsupportedLocale: When locale not supported.
        :return: Nothing.
        """
        pass

    def _extract(self, keys: list[str], default: t.Any=None) -> t.Any:
        """Extracts nested values from JSON file by list of keys.

        :param keys: List of keys (order extremely matters).
        :param default: Default value.
        :return: Data.
        """
        pass

    def _update_dict(self, initial: JSON, other: JSON) -> JSON:
        """Recursively updates a dictionary.

        :param initial: Dict to update.
        :param other: Dict to update from.
        :return: Updated dict.
        """
        pass

    def _load_dataset(self) -> None:
        """Loads the content from the JSON dataset.

        :return: The content of the file.
        :raises UnsupportedLocale: Raises if locale is unsupported.
        """
        pass

    def update_dataset(self, data: JSON) -> None:
        """Updates dataset merging a given dict into default data.

        This method may be useful when you need to override data
        for a given key in JSON file.
        """
        pass

    def get_current_locale(self) -> str:
        """Returns current locale.

        If locale is not defined, then this method will always return ``en``,
        because ``en`` is default locale for all providers, excluding builtins.

        :return: Current locale.
        """
        pass

    def _override_locale(self, locale: Locale=Locale.DEFAULT) -> None:
        """Overrides current locale with passed and pull data for new locale.

        :param locale: Locale
        :return: Nothing.
        """
        pass

    @contextlib.contextmanager
    def override_locale(self, locale: Locale) -> t.Generator['BaseDataProvider', None, None]:
        """Context manager that allows overriding current locale.

        Temporarily overrides current locale for
        locale-dependent providers.

        :param locale: Locale.
        :return: Provider with overridden locale.
        """
        pass

    def __str__(self) -> str:
        """Human-readable representation of locale."""
        locale = Locale(getattr(self, 'locale', Locale.DEFAULT))
        return f'{self.__class__.__name__} <{locale}>'