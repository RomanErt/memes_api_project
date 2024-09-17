import requests
import allure
from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    converted_to_json = None

    @allure.step('Get one meme by ID')
    def get_meme(self, meme_id, headers):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
        return self.response
