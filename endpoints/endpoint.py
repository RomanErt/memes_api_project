import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None

    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    @allure.step('Verify response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Verify error 404 received (negative scenario)')
    def check_bad_request_404(self):
        assert self.response.status_code == 404

    @allure.step('Verify error 401 - Unauthorized received (negative scenario')
    def check_bad_request_401(self):
        assert self.response.status_code == 401

    @allure.step('Verify error 403 - Forbidden received (negative scenario')
    def check_bad_request_403(self):
        assert self.response.status_code == 403
