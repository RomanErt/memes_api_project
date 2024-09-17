
def test_authorization_success(authorize_endpoint):
    response = authorize_endpoint.authorize()
    assert response is not None, "Authorization failed, no response"
    authorize_endpoint.check_that_status_is_200()


def test_get_a_meme(get_meme_endpoint_factory, new_meme_id, auth_header):
    get_meme_endpoint_factory.get_meme(meme_id=new_meme_id, headers=auth_header)
    get_meme_endpoint_factory.check_that_status_is_200()


def test_get_a_meme_unauthorized(get_meme_endpoint_factory, new_meme_id):
    get_meme_endpoint_factory.get_meme(meme_id=new_meme_id, headers=None)
    get_meme_endpoint_factory.check_bad_request_401()


def test_get_all_memes(get_all_memes_endpoint_factory, auth_header):
    get_all_memes_endpoint_factory.get_all_memes(headers=auth_header)
    get_all_memes_endpoint_factory.check_that_status_is_200()


def test_add_a_meme(post_meme_endpoint_factory, auth_header):
    body = {
        "info": {
            "colors": [
                "green",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "thanks"
        ],
        "text": "Thank you Eugene",
        "url": "https://giphy.com/gifs/thank-you-thanks-thumbs-up-BYoRqTmcgzHcL9TCy1"
    }
    post_meme_endpoint_factory.add_new_meme(payload=body, headers=auth_header)
    post_meme_endpoint_factory.check_that_status_is_200()
    post_meme_endpoint_factory.test_response_tag_is_correct(tags=[
            "fun",
            "thanks"
        ])


def test_add_a_meme_expect_400(post_meme_endpoint_factory, auth_header):
    body = {
        "info": {
            "colors": [
                "green",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "thanks"
        ],
        "url": "https://giphy.com/gifs/thank-you-thanks-thumbs-up-BYoRqTmcgzHcL9TCy1"
    }
    response = post_meme_endpoint_factory.add_new_meme(payload=body, headers=auth_header)
    if response:
        assert response.status_code == 100, f"Expected status code 400, got {response.status_code}"
    else:
        print(AssertionError("Failed to get a response from the API"))


def test_add_meme_unauthorized_user(post_meme_endpoint_factory):
    body = {
        "info": {
            "colors": [
                "green",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "thanks"
        ],
        "text": "Thank you Eugene",
        "url": "https://giphy.com/gifs/thank-you-thanks-thumbs-up-BYoRqTmcgzHcL9TCy1"
    }
    post_meme_endpoint_factory.add_new_meme(body, {'authorization': 'ferfrubb2122'})
    post_meme_endpoint_factory.check_bad_request_401()


def test_modify_meme_for_another_user(modify_meme_endpoint_factory, auth_header):
    body = {
        "id": 110,
        "info": {
            "colors": [
                "green",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "even more fun",
            "thank you"
        ],
        "text": "Here we go",
        "url": "https://giphy.com/gifs/thank-you-thanks-thumbs-up-BYoRqTmcgzHcL9TCy1"
    }
    modify_meme_endpoint_factory.modify_meme(meme_id=110, payload=body, headers=auth_header)
    modify_meme_endpoint_factory.check_bad_request_403()


def test_modify_meme(modify_meme_endpoint_factory, new_meme_id, auth_header):
    body = {
        "id": new_meme_id,
        "info": {
            "colors": [
                "green",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "even more fun",
            "thank you"
        ],
        "text": "Thank you Eugene",
        "url": "https://giphy.com/gifs/thank-you-thanks-thumbs-up-BYoRqTmcgzHcL9TCy1"
    }
    modify_meme_endpoint_factory.modify_meme(meme_id=new_meme_id, payload=body, headers=auth_header)
    modify_meme_endpoint_factory.test_updated_response_tag_is_correct(tags=[
            "even more fun",
            "thank you"
        ])
    modify_meme_endpoint_factory.test_response_info_is_correct(info={
            "colors": [
                "green",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        })


def test_delete_meme(delete_meme_endpoint_factory, new_meme_id, auth_header):
    delete_meme_endpoint_factory.delete_meme(meme_id=new_meme_id, headers=auth_header)
    delete_meme_endpoint_factory.check_that_status_is_200()
    delete_meme_endpoint_factory.delete_meme(meme_id=new_meme_id, headers=auth_header)
    delete_meme_endpoint_factory.check_bad_request_404()
