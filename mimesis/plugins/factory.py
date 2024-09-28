from contextlib import contextmanager
from typing import Any, ClassVar, Iterator
from mimesis.locales import Locale
from mimesis.schema import Field, RegisterableFieldHandlers
try:
    from factory import declarations
    from factory.builder import BuildStep, Resolver
except ImportError:
    raise ImportError('This plugin requires factory_boy to be installed.')
__all__ = ['FactoryField', 'MimesisField']

class FactoryField(declarations.BaseDeclaration):
    """
    Mimesis integration with FactoryBoy starts here.

    This class provides a common interface for FactoryBoy,
    but inside it has Mimesis generators.
    """
    _default_locale: ClassVar[Locale] = Locale.EN
    _cached_instances: ClassVar[dict[str, Field]] = {}

    def __init__(self, field: str, locale: Locale | None=None, **kwargs: Any) -> None:
        """
        Creates a field instance.

        The created field is lazy. It also receives build time parameters.
        These parameters are not applied yet.

        :param field: name to be passed to :class:`~mimesis.schema.Field`.
        :param locale: locale to use. This parameter has the highest priority.
        :param kwargs: optional parameters that would be passed to ``Field``.
        """
        super().__init__()
        self.locale = locale
        self.kwargs = kwargs
        self.field = field

    def evaluate(self, instance: Resolver, step: BuildStep, extra: dict[str, Any] | None=None) -> Any:
        """Evaluates the lazy field.

        :param instance: (factory.builder.Resolver): The object holding currently computed attributes.
        :param step: (factory.builder.BuildStep): The object holding the current build step.
        :param extra: Extra call-time added kwargs that would be passed to ``Field``.
        """
        pass

    @classmethod
    @contextmanager
    def override_locale(cls, locale: Locale) -> Iterator[None]:
        """
        Overrides unspecified locales.

        Remember that implicit locales would not be overridden.
        """
        pass

    @classmethod
    def _get_cached_instance(cls, locale: Locale | None=None, field_handlers: RegisterableFieldHandlers | None=None) -> Field:
        """Returns cached instance.

        :param locale: locale to use.
        :param field_handlers: custom field handlers.
        :return: cached instance of Field.
        """
        pass
MimesisField = FactoryField