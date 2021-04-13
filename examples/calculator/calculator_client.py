import sys
import time
from enum import Enum

import calculator.api as api

from zserio_service_http import HttpClient

class Mode(Enum):
    POWER_OF_TWO = 1
    SQUARE_ROOT = 2

def _print_help():
    print(
        "Help:",
        " INPUT        Any valid input for the current mode.",
        " p            Sets powerOfTwo(int32) mode.",
        " s            Sets squareRoot(double) mode.",
        " h            Prints this help.",
        " q            Quits the client.",
        "",
        "Note that the letter before the '>' denotes the current mode.",
        sep='\n'
    )

def _power_of_two(client: api.Calculator.Client, line: str):
    try:
        request = api.I32(int(line))
    except Exception as expt:
        print("Error: '%s' cannot be converted to int32!" % line)
        print(expt)

        return

    try:
        response = client.power_of_two(request)
    except Exception as expt:
        print("Error:", expt)
    else:
        print(response.value)

def _square_root(client: api.Calculator.Client, line: str):
    try:
        request = api.Double(float(line))
    except Exception as expt:
        print("Error: '%s' cannot be converted to double!" % line)
        print(expt)

        return

    try:
        response = client.square_root(request)
    except Exception as expt:
        print("Error:", expt)
    else:
        print(response.value)

def _main():
    address = sys.argv[1] if len(sys.argv) > 1 else "localhost:5000"
    (host, port) = address.split(':') if ':' in address else (address, "5000")

    print("Welcome to Zserio Calculator HTTP Client example!")
    print("Waiting for connection (terminate with ^C) ...", end='', flush=True)

    # HttpClient from zserio_service_http library
    http_client = HttpClient(api.Calculator.Service().service_full_name, host, int(port))
    # Calculator client generated by Zserio, uses http_client as the service
    client = api.Calculator.Client(http_client)

    print(" OK!")
    print("Write 'h' + ENTER for help.")

    mode = Mode.POWER_OF_TWO

    while True:
        line = input(('p' if mode == Mode.POWER_OF_TWO else 's') + "> ")
        if not line:
            continue

        if line[0] == 'q':
            print("Quiting.")
            time.sleep(1) # wait a little bit for a potential responses
            sys.exit(0)

        if line[0] == 'h':
            _print_help()
            continue

        if line[0] == 'p':
            mode = Mode.POWER_OF_TWO
            print("Mode set to powerOfTwo(int32)")
            continue

        if line[0] == 's':
            mode = Mode.SQUARE_ROOT
            print("Mode set to squareRoot(double)")
            continue

        if mode == Mode.POWER_OF_TWO:
            _power_of_two(client, line)
        else:
            _square_root(client, line)

if __name__ == "__main__":
    sys.exit(_main())
