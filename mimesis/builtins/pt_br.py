"""Specific data provider for Brazil (pt-br)."""
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed
__all__ = ['BrazilSpecProvider']

class BrazilSpecProvider(BaseDataProvider):
    """Class that provides special data for Brazil (pt-br)."""

    def __init__(self, seed: Seed=MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.PT_BR, seed=seed)

    class Meta:
        name = 'brazil_provider'
        datafile = None

    @staticmethod
    def __get_verifying_digit_cpf(cpf: list[int], weight: int) -> int:
        """Calculate the verifying digit for the CPF.

        :param cpf: List of integers with the CPF.
        :param weight: Integer with the weight for the modulo 11 calculate.
        :returns: The verifying digit for the CPF.
        """
        pass

    def cpf(self, with_mask: bool=True) -> str:
        """Get a random CPF.

        :param with_mask: Use CPF mask (###.###.###-##).
        :returns: Random CPF.

        :Example:
            001.137.297-40
        """
        pass

    @staticmethod
    def __get_verifying_digit_cnpj(cnpj: list[int], weight: int) -> int:
        """Calculate the verifying digit for the CNPJ.

        :param cnpj: List of integers with the CNPJ.
        :param weight: Integer with the weight for the modulo 11 calculate.
        :returns: The verifying digit for the CNPJ.
        """
        pass

    def cnpj(self, with_mask: bool=True) -> str:
        """Get a random CNPJ.

        :param with_mask: Use cnpj mask (###.###.###-##)
        :returns: Random cnpj.

        :Example:
            77.732.230/0001-70
        """
        pass