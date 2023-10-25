import sys
import math
import typing

from calculator import api

from zserio_service_http import HttpServer

class CalculatorService(api.Calculator.Service):
    """
    Implementation of Zserio Calculator Service.
    """

    def _power_of_two_impl(self, request: api.I32, _context: typing.Any = None) -> api.U64:
        response = api.U64(request.value**2)
        return response

    def _square_root_impl(self, request: api.Double, _context: typing.Any = None) -> api.Double:
        response = api.Double(math.sqrt(request.value))
        return response

def _main():
    address = sys.argv[1] if len(sys.argv) > 1 else "localhost:5000"
    (host, port) = address.split(':') if ':' in address else (address, "5000")

    calculator_service = CalculatorService()
    # HttpServer from zserio_service_http library uses the Zserio Calculator Service
    http_server = HttpServer(calculator_service)
    http_server.run(host, int(port))

if __name__ == "__main__":
    sys.exit(_main())
