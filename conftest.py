import pytest
from endpoints.authorization import Authorization
from endpoints.get_meme import GetMeme
from endpoints.get_all_memes import GetAllMemes
from endpoints.post_meme import PostMeme
from endpoints.modify_meme import ModifyMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.endpoint import Endpoint


@pytest.fixture(scope="session")
def authorize_endpoint():
    return Authorization(url=Endpoint.url)


@pytest.fixture()
def get_meme_endpoint_factory(auth_header):
    return GetMeme(auth_token=auth_header['authorization'])


@pytest.fixture()
def get_all_memes_endpoint_factory(auth_header):
    return GetAllMemes(auth_token=auth_header['authorization'])


@pytest.fixture()
def post_meme_endpoint_factory(auth_header):
    return PostMeme(auth_token=auth_header['authorization'])


@pytest.fixture()
def modify_meme_endpoint_factory(auth_header):
    return ModifyMeme(auth_token=auth_header['authorization'])


@pytest.fixture()
def delete_meme_endpoint_factory(auth_header):
    return DeleteMeme(auth_token=auth_header['authorization'])


@pytest.fixture()
def new_meme_id(post_meme_endpoint_factory, auth_header):
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
    post_meme_endpoint_factory.add_new_meme(body, headers=auth_header)
    meme_id = post_meme_endpoint_factory.meme_id
    yield meme_id
    post_meme_endpoint_factory.delete_meme(meme_id, headers=auth_header)


@pytest.fixture(scope="session")
def auth_header(authorize_endpoint):
    response = authorize_endpoint.authorize()
    if response and 'authorization' in response:
        return {'authorization': response['authorization']}
    else:
        raise Exception("Failed to retrieve authorization token")
