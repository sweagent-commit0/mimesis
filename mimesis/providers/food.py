"""Provides data related to food."""
from mimesis.providers.base import BaseDataProvider
__all__ = ['Food']

class Food(BaseDataProvider):
    """Class for generating data related to food."""

    class Meta:
        name = 'food'
        datafile = f'{name}.json'

    def _choice_from(self, key: str) -> str:
        """Choice random element."""
        pass

    def vegetable(self) -> str:
        """Generates a random vegetable name.

        :return: Vegetable name.

        :Example:
            Tomato.
        """
        pass

    def fruit(self) -> str:
        """Generates a random fruit or berry name.

        :return: Fruit name.

        :Example:
            Banana.
        """
        pass

    def dish(self) -> str:
        """Generates a random dish name.

        :return: Dish name.

        :Example:
            Ratatouille.
        """
        pass

    def spices(self) -> str:
        """Generates a random spices/herb name.

        :return: The name of the spices or herbs.

        :Example:
            Anise.
        """
        pass

    def drink(self) -> str:
        """Generates a random drink name.

        :return: Drink name.

        :Example:
            Vodka.
        """
        pass