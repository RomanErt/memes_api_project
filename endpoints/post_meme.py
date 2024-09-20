import requests
import allure
import logging
from endpoints.endpoint import Endpoint


class PostMeme(Endpoint):
    def __init__(self, auth_token=None):
        super().__init__(auth_token)
        self.converted_to_json = None
        self.meme_id = None

    @allure.step('Add a new meme')
    def add_new_meme(self, payload, headers):
        try:
            self.response = requests.post(f'{self.url}/meme', json=payload, headers=headers)
            self.response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to post meme: {e}")
            return None

        try:
            self.converted_to_json = self.response.json()
            self.meme_id = self.converted_to_json["id"]
        except ValueError:
            logging.warning("Failed to decode JSON from response")
            self.converted_to_json = None

        return self.response

    def delete_meme(self, meme_id, headers):
        response = requests.delete(f"{self.url}/meme/{meme_id}", headers=headers)
        return response
