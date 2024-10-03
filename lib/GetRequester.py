import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request to the URL
        response = requests.get(self.url)
        # Raise an error for bad responses (4xx or 5xx)
        response.raise_for_status()
        # Return the body of the response
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
         #Parse the response body as JSON and return it
        return json.loads(response_body)