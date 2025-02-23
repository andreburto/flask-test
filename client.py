import json
import requests
import sys


DEFAULT_URL = "http://localhost:8000"


class Incrementer:
    """
    A class to interact with the incrementer API server.
    This is a simple test to try out a functional use of requests.
    """
    def __init__(self, url=DEFAULT_URL):
        self.url = url

    def _call_api(self, method, path, data=None):
        response = method(f"{self.url}/{path}", data=data)
        return response.json()

    def get_value(self):
        return self._call_api(requests.get, "")

    def increment(self, value=1):
        return self._call_api(requests.put, f"inc/{value}")

    def decrement(self, value=1):
        return self._call_api(requests.put, f"dec/{value}")

    def reset(self):
        return self._call_api(requests.put, f"reset")


def main():
    """
    A simple command line interface to interact with the incrementer API.
    """

    # Get the command from the command line arguments, default to "get"
    command = "get" if len(sys.argv) < 2 else sys.argv[1]

    if command not in ["get", "inc", "dec", "reset"]:
        print("Invalid command")
        sys.exit(1)

    if command in ["inc", "dec"] and len(sys.argv) < 3:
        print("Please provide a value to increment or decrement by")
        sys.exit(1)

    incrementer = Incrementer()

    # Map the command to the function to call.
    # TODO: Move this to a static method in the Incrementer class.
    call_by_command = {
        "get": "get_value",
        "inc": "increment",
        "dec": "decrement",
        "reset": "reset",
    }
    function_to_call = getattr(incrementer, call_by_command[command])

    # TODO: Find a more Pythonic way to do this.
    if command in ["inc", "dec"]:
        results = function_to_call(int(sys.argv[2]))
    else:
        results = function_to_call()

    print(f"Results: {results}")

if __name__ == "__main__":
    main()
