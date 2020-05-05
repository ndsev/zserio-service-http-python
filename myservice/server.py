import sys

# Make zserio runtime available
import zserio

# Use HTTP base RPC mechanism
from myservice.http_rpc import HttpServer

# Import zserio-generated API
import myservice.zs
from zs_api.myservice import MyService
from zs_api.myservice.Answer import Answer


class DrKnow(MyService.Service):
    def _askImpl(self, request, _context):
        print("A got a very good question: " + request.getText())
        response = Answer.fromFields("All I know is that I know nothing.")
        return response


if __name__ == "__main__":
    answerService = DrKnow()
    httpServer = HttpServer(answerService)
    httpServer.run("localhost", 5000)
