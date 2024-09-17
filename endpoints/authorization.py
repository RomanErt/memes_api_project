import requests
import allure
from endpoints.endpoint import Endpoint


class Authorization(Endpoint):

    @allure.step("Issuing authorization token")
    def authorize(self):
        self.response = None
        body = {'name': 'My_auth_token'}
        try:
            self.response = requests.post(f'{self.url}/authorize', json=body)
            self.response.raise_for_status()
            token = self.response.json()['token']
            return {'authorization': token}
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except ValueError:
            print("Failed to decode JSON from response")
        return self.response
