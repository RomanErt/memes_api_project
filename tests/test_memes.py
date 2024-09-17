from tests.test_data import invalid_token, TEST_BODY_POSITIVE, TEST_BODY_NEGATIVE, TEST_BODY_UPDATE_POSITIVE


def test_authorization_success(authorize_endpoint):
    authorize_endpoint.authorize()
    authorize_endpoint.check_that_status_is_200()
    authorize_endpoint.verify_token_not_empty()


def test_get_a_meme(get_meme_endpoint_factory, new_meme_id, auth_header):
    get_meme_endpoint_factory.get_meme(meme_id=new_meme_id, headers=auth_header)
    get_meme_endpoint_factory.check_that_status_is_200()


def test_get_a_meme_unauthorized(get_meme_endpoint_factory, new_meme_id):
    get_meme_endpoint_factory.get_meme(meme_id=new_meme_id, headers=None)
    get_meme_endpoint_factory.report_errors()
    get_meme_endpoint_factory.check_unauthorized_401()


def test_get_all_memes(get_all_memes_endpoint_factory, auth_header):
    get_all_memes_endpoint_factory.get_all_memes(headers=auth_header)
    get_all_memes_endpoint_factory.check_that_status_is_200()


def test_add_a_meme(post_meme_endpoint_factory, auth_header):
    body = TEST_BODY_POSITIVE
    post_meme_endpoint_factory.add_new_meme(payload=body, headers=auth_header)
    post_meme_endpoint_factory.check_that_status_is_200()
    post_meme_endpoint_factory.test_response_text_is_correct(text=body['text'])
    post_meme_endpoint_factory.test_response_tags_are_correct(tags=body['tags'])
    post_meme_endpoint_factory.test_response_info_is_correct(info=body['info'])


def test_add_a_meme_missing_body_text(post_meme_endpoint_factory, auth_header):
    post_meme_endpoint_factory.add_new_meme(payload=TEST_BODY_NEGATIVE, headers=auth_header)
    post_meme_endpoint_factory.report_errors()


def test_add_meme_unauthorized_user(post_meme_endpoint_factory):
    post_meme_endpoint_factory.add_new_meme(TEST_BODY_POSITIVE, {'authorization': invalid_token})
    post_meme_endpoint_factory.check_unauthorized_401()
    post_meme_endpoint_factory.report_errors()


def test_modify_meme_for_another_user(modify_meme_endpoint_factory, auth_header):
    meme_id = 110
    modify_meme_endpoint_factory.modify_meme(meme_id=meme_id, payload=TEST_BODY_UPDATE_POSITIVE, headers=auth_header)
    modify_meme_endpoint_factory.report_errors()
    modify_meme_endpoint_factory.check_bad_request_403()


def test_modify_meme(modify_meme_endpoint_factory, new_meme_id, auth_header):
    body = TEST_BODY_UPDATE_POSITIVE
    body["id"] = new_meme_id
    modify_meme_endpoint_factory.modify_meme(meme_id=new_meme_id, payload=body, headers=auth_header)
    modify_meme_endpoint_factory.test_updated_response_tag_is_correct(tags=body['tags'])
    modify_meme_endpoint_factory.test_response_info_is_correct(info=body['info'])


def test_delete_meme(delete_meme_endpoint_factory, new_meme_id, auth_header):
    delete_meme_endpoint_factory.delete_meme(meme_id=new_meme_id, headers=auth_header)
    delete_meme_endpoint_factory.check_that_status_is_200()
    delete_meme_endpoint_factory.delete_meme(meme_id=new_meme_id, headers=auth_header)
    delete_meme_endpoint_factory.check_bad_request_404()
