import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    converted_to_json = None
    meme_id = None

    @allure.step('Delete the meme')
    def delete_meme(self, meme_id, headers):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}', headers=headers
        )
        return self.response
