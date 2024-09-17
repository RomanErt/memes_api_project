import requests
import allure
from endpoints.endpoint import Endpoint


class Authorization(Endpoint):

    def __init__(self, url):
        super().__init__(url)
        self.token = None

    @allure.step("Issuing authorization token")
    def authorize(self):
        self.response = None
        body = {'name': 'My_auth_token'}
        try:
            self.response = requests.post(f'{self.url}/authorize', json=body)
            self.response.raise_for_status()
            self.token = self.response.json()['token']
            return {'authorization': self.token}
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except ValueError:
            print("Failed to decode JSON from response")
        return self.response

    @allure.step("Verify response token is not empty")
    def verify_token_not_empty(self):
        assert self.token is not None, "Token should not be empty"
