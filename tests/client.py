import requests
import json

class Client:
    """
    client that implement interface request
    """
    def make_request(self,address='http://localhost:5000/number'):
        response = requests.get(address)
        return json.loads(response.text)
