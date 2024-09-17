import requests
import allure
from endpoints.endpoint import Endpoint
from requests.exceptions import JSONDecodeError


class ModifyMeme(Endpoint):
    converted_to_json = None

    @allure.step('Modify tags for an existing meme')
    def modify_meme(self, meme_id, payload, headers):
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}', json=payload, headers=headers
        )
        try:
            self.converted_to_json = self.response.json()
        except JSONDecodeError:
            self.converted_to_json = None
        return self.response

    @allure.step('Verify updated meme tags are correct')
    def test_updated_response_tag_is_correct(self, tags):
        assert self.converted_to_json['tags'] == tags

    @allure.step('Verify info is correct')
    def test_response_info_is_correct(self, info):
        assert self.converted_to_json['info'] == info
