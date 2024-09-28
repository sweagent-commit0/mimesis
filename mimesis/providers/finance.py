"""Business data provider."""
from mimesis.datasets import CRYPTOCURRENCY_ISO_CODES, CRYPTOCURRENCY_SYMBOLS, CURRENCY_ISO_CODES, CURRENCY_SYMBOLS, STOCK_EXCHANGES, STOCK_NAMES, STOCK_TICKERS
from mimesis.providers.base import BaseDataProvider
__all__ = ['Finance']

class Finance(BaseDataProvider):
    """Class to generate finance and business related data."""

    class Meta:
        name = 'finance'
        datafile = f'{name}.json'

    def company(self) -> str:
        """Generates a random company name.

        :return: Company name.
        """
        pass

    def company_type(self, abbr: bool=False) -> str:
        """Generates a random type of business entity.

        :param abbr: Abbreviated company type.
        :return: Types of business entity.
        """
        pass

    def currency_iso_code(self, allow_random: bool=False) -> str:
        """Returns a currency code for current locale.

        :param allow_random: Get a random ISO code.
        :return: Currency code.
        """
        pass

    def bank(self) -> str:
        """Generates a random bank name.

        :return: Bank name.
        """
        pass

    def cryptocurrency_iso_code(self) -> str:
        """Generates a random cryptocurrency ISO code.

        :return: Symbol of cryptocurrency.
        """
        pass

    def currency_symbol(self) -> str:
        """Returns a currency symbol for current locale.

        :return: Currency symbol.
        """
        pass

    def cryptocurrency_symbol(self) -> str:
        """Get a cryptocurrency symbol.

        :return: Symbol of cryptocurrency.
        """
        pass

    def price(self, minimum: float=500, maximum: float=1500) -> float:
        """Generate a random price.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :return: Price.
        """
        pass

    def price_in_btc(self, minimum: float=0, maximum: float=2) -> float:
        """Generates a random price in BTC.

        :param minimum: Minimum value of price.
        :param maximum: Maximum value of price.
        :return: Price in BTC.
        """
        pass

    def stock_ticker(self) -> str:
        """Generates a random stock ticker.

        :return: Ticker.
        """
        pass

    def stock_name(self) -> str:
        """Generates a stock name.

        :return: Stock name.
        """
        pass

    def stock_exchange(self) -> str:
        """Generates a stock exchange name.

        :return: Returns exchange name.
        """
        pass