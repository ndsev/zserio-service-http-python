from flask import Flask, request

import zserio

class HttpServer:
    """
    Implementation of the HTTP server.

    HttpServer creates a HTTP server for a particular Zserio service implementation.
    """

    def __init__(self, service_impl: zserio.ServiceInterface):
        """
        Constructor.

        :param service_impl: Implementation of a particular Zserio service.
        """

        self._service_impl = service_impl
        self._app = Flask(service_impl.service_full_name)

        # pylint: disable=unused-variable
        @self._app.route('/' + service_impl.service_full_name.replace('.', '/') + "/<methodName>",
                         methods=['POST'])
        def call_method(method_name: str) -> bytes:
            request_data = request.get_data()
            response = self._service_impl.call_method(method_name, request_data)

            return response.byte_array

    def run(self, host:str = "localhost", port:int = 5000):
        """
        Runs the HTTP server.

        :param host: Host to use for the HTTP server.
        :param port: Port on which the server will be listening.
        """

        self._app.run(host, port)
