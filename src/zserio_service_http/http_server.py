from flask import Flask, request

class HttpServer:
    """
    Implementation of the HTTP server.

    HttpServer creates a HTTP server for a particular Zserio service implementation.
    """

    def __init__(self, serviceImpl):
        """
        Constructor.

        :param serviceImpl: Implementation of a particular Zserio service.
        """

        self.serviceImpl = serviceImpl
        self.app = Flask(serviceImpl.SERVICE_FULL_NAME)

        @self.app.route('/' + serviceImpl.SERVICE_FULL_NAME.replace('.', '/') + "/<methodName>",
                        methods=['POST'])
        def callMethod(methodName):
            requestData = request.get_data()
            responseData = self.serviceImpl.callMethod(methodName, requestData)
            return responseData

    def run(self, host="localhost", port="5000"):
        """
        Runs the HTTP server.

        :param host: Host to use for the HTTP server.
        :param port: Port on which the server will be listening.
        """

        self.app.run(host, port)
