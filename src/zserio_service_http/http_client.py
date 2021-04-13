import typing
import http.client
from http import HTTPStatus

import zserio

class HttpClient(zserio.ServiceClientInterface):
    """
    Implementation of HTTP client as Zserio generic service interface.
    """

    def __init__(self, service_full_name: str, host: str = "localhost", port:int = 5000):
        """
        Constructor.

        :param service_full_name: Full name of the Zserio service (needed to construct a REST-like path).
        :param host: Host to connect.
        :param port: Port to connect.
        """

        self._connection = http.client.HTTPConnection(host, port)
        self._service_full_path = '/' + service_full_name.replace('.', '/') + '/'

    def call_method(self, method_name: str, request: zserio.ServiceData, _context: typing.Any = None) -> bytes:
        """
        Implementation of ServiceClientInterface.call_method.
        """

        try:
            self._connection.request("POST", self._service_full_path + method_name, request.byte_array)
            response = self._connection.getresponse()
            if response.status != HTTPStatus.OK:
                raise zserio.ServiceException(str(response.status))
            response_data = response.read()

            return response_data
        except Exception as expt:
            raise zserio.ServiceException("HTTP call failed: " + str(expt))
