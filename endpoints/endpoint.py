import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'

    def __init__(self, auth_token=None):
        self.auth_token = auth_token
        self.response = None
        self.errors = []

    @allure.step('Verify response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Verify error 404 received (negative scenario)')
    def check_bad_request_404(self):
        assert self.response.status_code == 404

    @allure.step('Verify error 401 - Unauthorized received (negative scenario')
    def check_unauthorized_401(self):
        assert self.response.status_code == 401

    @allure.step('Verify error 403 - Forbidden received (negative scenario')
    def check_forbidden_403(self):
        assert self.response.status_code == 403

    @allure.step('Verify response text is correct')
    def test_response_text_is_correct(self, text):
        assert self.response.json()["text"] == text

    @allure.step('Verify response tags are correct')
    def test_response_tags_are_correct(self, tags):
        assert self.response.json()["tags"] == tags

    @allure.step('Verify response info is correct')
    def test_response_info_is_correct(self, info):
        assert self.response.json()['info'] == info

    @allure.step('Report errors during the test execution')
    def report_errors(self):
        if self.errors:
            report = '\n'.join(self.errors)
            raise AssertionError(f'Failed with the following errors: {report}')
