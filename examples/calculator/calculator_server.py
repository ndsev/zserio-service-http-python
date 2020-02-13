import sys
import math

import zserio
from zserio_service_http import HttpServer
import calculator.api as api

class CalculatorService(api.Calculator.Service):
    """
    Implementation of Zserio Calculator Service.
    """

    def _powerOfTwoImpl(self, request, _context):
        response = api.U64.fromFields(request.getValue()**2)
        return response

    def _squareRootImpl(self, request, _context):
        response = api.Double.fromFields(math.sqrt(request.getValue()))
        return response

if __name__ == "__main__":
    address = sys.argv[1] if len(sys.argv) > 1 else "localhost:5000"
    (host, port) = address.split(':') if ':' in address else (address, 5000)

    calculatorService = CalculatorService()
    # HttpServer from zserio_service_http library uses the Zserio Calculator Service
    httpServer = HttpServer(calculatorService)
    httpServer.run(host, port)
