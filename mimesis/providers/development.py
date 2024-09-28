"""Data related to the development."""
import typing as t
from datetime import datetime
from mimesis.datasets import LICENSES, OS, PROGRAMMING_LANGS, STAGES, SYSTEM_QUALITY_ATTRIBUTES
from mimesis.providers.base import BaseProvider
__all__ = ['Development']

class Development(BaseProvider):
    """Class for getting fake data for Developers."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        name = 'development'

    def software_license(self) -> str:
        """Generates a random software license.

        :return: License name.

        :Example:
            The BSD 3-Clause License.
        """
        pass

    def calver(self) -> str:
        """Generates a random calendar versioning string.

        :return: Calendar versioning string.

        :Example:
            2016.11.08
        """
        pass

    def version(self) -> str:
        """Generates a random semantic versioning string.

        :return: Semantic versioning string.

        :Example:
            0.2.1
        """
        pass

    def stage(self) -> str:
        """Generates a random stage of development.

        :return: Release stage.

        :Example:
            Alpha.
        """
        pass

    def programming_language(self) -> str:
        """Generates a random programming language from the list.

        :return: Programming language.

        :Example:
            Erlang.
        """
        pass

    def os(self) -> str:
        """Generates a random operating system or distributive name.

        :return: The name of OS.

        :Example:
            Gentoo
        """
        pass

    def boolean(self) -> bool:
        """Generates a random boolean value.

        :return: True of False.
        """
        pass

    def system_quality_attribute(self) -> str:
        """Generates a random system quality attribute.

        Within systems engineering, quality attributes are realized
        non-functional requirements used to evaluate the performance
        of a system. These are sometimes named "ilities" after the
        suffix many of the words share.

        :return: System quality attribute.
        """
        pass

    def ility(self) -> str:
        """Generates a random system quality attribute.

        An alias for :meth:`~mimesis.Development.system_quality_attribute`.
        """
        pass