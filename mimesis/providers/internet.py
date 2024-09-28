"""Provides data related to internet."""
import typing as t
import urllib.error
import urllib.parse
import urllib.request
from base64 import b64encode
from ipaddress import IPv4Address, IPv6Address
from mimesis.datasets import CONTENT_ENCODING_DIRECTIVES, CORS_OPENER_POLICIES, CORS_RESOURCE_POLICIES, HTTP_METHODS, HTTP_SERVERS, HTTP_STATUS_CODES, HTTP_STATUS_MSGS, PUBLIC_DNS, TLD, USER_AGENTS, USERNAMES
from mimesis.enums import DSNType, Locale, MimeType, PortRange, TLDType, URLScheme
from mimesis.providers.base import BaseProvider
from mimesis.providers.code import Code
from mimesis.providers.date import Datetime
from mimesis.providers.file import File
from mimesis.providers.text import Text
from mimesis.types import Keywords
__all__ = ['Internet']

class Internet(BaseProvider):
    """Class for generating data related to the internet."""
    _MAX_IPV4: t.Final[int] = 2 ** 32 - 1
    _MAX_IPV6: t.Final[int] = 2 ** 128 - 1

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._file = File(seed=self.seed, random=self.random)
        self._code = Code(seed=self.seed, random=self.random)
        self._text = Text(locale=Locale.EN, seed=self.seed, random=self.random)
        self._datetime = Datetime(locale=Locale.EN, seed=self.seed, random=self.random)

    class Meta:
        name = 'internet'

    def content_type(self, mime_type: MimeType | None=None) -> str:
        """Generates a random HTTP content type.

        :return: Content type.

        :Example:
            application/json
        """
        pass

    def dsn(self, dsn_type: DSNType | None=None, **kwargs: t.Any) -> str:
        """Generates a random DSN (Data Source Name).

        :param dsn_type: DSN type.
        :param kwargs: Additional keyword-arguments for hostname method.
        """
        pass

    def http_status_message(self) -> str:
        """Generates a random HTTP status message.

        :return: HTTP status message.

        :Example:
            200 OK
        """
        pass

    def http_status_code(self) -> int:
        """Generates a random HTTP status code.

        :return: HTTP status.

        :Example:
            200
        """
        pass

    def http_method(self) -> str:
        """Generates a random HTTP method.

        :return: HTTP method.

        :Example:
            POST
        """
        pass

    def ip_v4_object(self) -> IPv4Address:
        """Generates a random :py:class:`ipaddress.IPv4Address` object.

        :return: :py:class:`ipaddress.IPv4Address` object.
        """
        pass

    def ip_v4_with_port(self, port_range: PortRange=PortRange.ALL) -> str:
        """Generates a random IPv4 address as string.

        :param port_range: PortRange enum object.
        :return: IPv4 address as string.

        :Example:
            19.121.223.58:8000
        """
        pass

    def ip_v4(self) -> str:
        """Generates a random IPv4 address as string.

        :Example:
            19.121.223.58
        """
        pass

    def ip_v6_object(self) -> IPv6Address:
        """Generates random :py:class:`ipaddress.IPv6Address` object.

        :return: :py:class:`ipaddress.IPv6Address` object.
        """
        pass

    def ip_v6(self) -> str:
        """Generates a random IPv6 address as string.

        :return: IPv6 address string.

        :Example:
            2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3
        """
        pass

    def mac_address(self) -> str:
        """Generates a random MAC address.

        :return: Random MAC address.

        :Example:
            00:16:3e:25:e7:f1
        """
        pass

    @staticmethod
    def stock_image_url(width: int | str=1920, height: int | str=1080, keywords: Keywords | None=None) -> str:
        """Generates a random stock image URL hosted on Unsplash.

        See «Random search term» on https://source.unsplash.com/
        for more details.

        :param width: Width of the image.
        :param height: Height of the image.
        :param keywords: Sequence of search keywords.
        :return: URL of the image.
        """
        pass

    def hostname(self, tld_type: TLDType | None=None, subdomains: list[str] | None=None) -> str:
        """Generates a random hostname without a scheme.

        :param tld_type: TLDType.
        :param subdomains: List of subdomains (make sure they are valid).
        :return: Hostname.
        """
        pass

    def url(self, scheme: URLScheme | None=URLScheme.HTTPS, port_range: PortRange | None=None, tld_type: TLDType | None=None, subdomains: list[str] | None=None) -> str:
        """Generates a random URL.

        :param scheme: The scheme.
        :param port_range: PortRange enum object.
        :param tld_type: TLDType.
        :param subdomains: List of subdomains (make sure they are valid).
        :return: URL.
        """
        pass

    def uri(self, scheme: URLScheme | None=URLScheme.HTTPS, tld_type: TLDType | None=None, subdomains: list[str] | None=None, query_params_count: int | None=None) -> str:
        """Generates a random URI.

        :param scheme: Scheme.
        :param tld_type: TLDType.
        :param subdomains: List of subdomains (make sure they are valid).
        :param query_params_count: Query params.
        :return: URI.
        """
        pass

    def query_string(self, length: int | None=None) -> str:
        """Generates an arbitrary query string of given length.

        :param length: Length of query string.
        :return: Query string.
        """
        pass

    def query_parameters(self, length: int | None=None) -> dict[str, str]:
        """Generates an arbitrary query parameters as a dict.

        :param length: Length of query parameters dictionary (maximum is 32).
        :return: Dict of query parameters.
        """
        pass

    def top_level_domain(self, tld_type: TLDType=TLDType.CCTLD) -> str:
        """Generates random top level domain.

        :param tld_type: Enum object :class:`enums.TLDType`
        :return: Top level domain.
        :raises NonEnumerableError: if tld_type not in :class:`enums.TLDType`.
        """
        pass

    def tld(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random TLD.

        An alias for :meth:`top_level_domain`
        """
        pass

    def user_agent(self) -> str:
        """Get a random user agent.

        :return: User agent.

        :Example:
            Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)
            Gecko/20100101 Firefox/15.0.1
        """
        pass

    def port(self, port_range: PortRange=PortRange.ALL) -> int:
        """Generates a random port.

        :param port_range: PortRange enum object.
        :return: Port number.
        :raises NonEnumerableError: if port_range is not in PortRange.

        :Example:
            8080
        """
        pass

    def path(self, *args: t.Any, **kwargs: t.Any) -> str:
        """Generates a random path.

        :param args: Arguments to pass to :meth:`slug`.
        :param kwargs: Keyword arguments to pass to :meth:`slug`.
        :return: Path.
        """
        pass

    def slug(self, parts_count: int | None=None) -> str:
        """Generates a random slug of given parts count.

        :param parts_count: Slug's parts count.
        :return: Slug.
        """
        pass

    def public_dns(self) -> str:
        """Generates a random public DNS.

        :Example:
            1.1.1.1
        """
        pass

    def http_response_headers(self) -> dict[str, t.Any]:
        """Generates a random HTTP response headers.

        The following headers are included:

        - Allow
        - Age
        - Server
        - Content-Type
        - X-Request-ID
        - Content-Language
        - Content-Location
        - Set-Cookie
        - Upgrade-Insecure-Requests
        - X-Content-Type-Options
        - X-XSS-Protection
        - Connection
        - X-Frame-Options
        - Content-Encoding
        - Cross-Origin-Opener-Policy
        - Cross-Origin-Resource-Policy
        - Strict-Transport-Security

        :return: Response headers as dict.
        """
        pass

    def http_request_headers(self) -> dict[str, t.Any]:
        """Generates a random HTTP request headers.

        The following headers are included:

        - Referer
        - Authorization
        - Cookie
        - User-Agent
        - X-CSRF-Token
        - Content-Type
        - Content-Length
        - Connection
        - Cache-Control
        - Accept
        - Host
        - Accept-Language

        :return: Request headers as dict.
        """
        pass