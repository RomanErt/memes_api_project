import requests
import allure
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    converted_to_json = None

    @allure.step('Get a list of all memes')
    def get_all_memes(self, headers):
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        return self.response
