import sys

# Make zserio runtime available
import zserio

# Import needed aspects of generated API
import myservice.zs
from zs_api.myservice import MyService
from zs_api.myservice.Question import Question

# Import used RPC mechanism
from myservice.http_rpc import HttpClient

if __name__ == "__main__":
    httpClient = HttpClient(MyService.Service.SERVICE_FULL_NAME, "localhost", 5000)
    client = MyService.Client(httpClient)

    print("Enter a question and get an answer ...")
    while True:
        line = input("> ")
        if not line:
            continue

        if line[0] == 'q':
            print("Quit.")
            exit(0)

        request = Question.fromFields(text_=line)
        try:
            response = client.askMethod(request)
        except Exception as e:
            print("Error:", e)
        else:
            print(response.getText())

