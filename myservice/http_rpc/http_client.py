import http.client
from http import HTTPStatus
import zserio

class HttpClient(zserio.ServiceInterface):
    """
    Implementation of HTTP client as Zserio generic service interface.
    """

    def __init__(self, serviceFullName, host="localhost", port=5000):
        """
        Constructor.

        :param serviceFullName: Full name of the Zserio service (needed to construct a REST-like path).
        :param host: Host to connect.
        :param port: Port to connect.
        """

        self.connection = http.client.HTTPConnection(host, port)
        self.serviceFullPath = '/' + serviceFullName.replace('.', '/') + '/'

    def callMethod(self, methodName, requestData, _context):
        """
        Implementation of ServiceInterface.callMethod.
        """

        try:
            self.connection.request("POST", self.serviceFullPath + methodName, requestData)
            response = self.connection.getresponse()
            if response.status != HTTPStatus.OK:
                raise zserio.ServiceException(str(response.status))
            responseData = response.read()
            return responseData
        except Exception as e:
            raise zserio.ServiceException("HTTP call failed: " + str(e))
