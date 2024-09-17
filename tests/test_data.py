invalid_token = 'dfdbfddfvv111'


TEST_BODY_POSITIVE = {
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

TEST_BODY_NEGATIVE = {
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

TEST_BODY_UPDATE_POSITIVE = {
        "id": 110,
        "info": {
            "colors": [
                "white",
                "black",
            ],
            "objects": [
                "picture",
            ]
        },
        "tags": [
            "even more fun",
            "thank you"
        ],
        "text": "Here we go",
        "url": "https://giphy.com/gifs/thank-you-thanks-thumbs-up-BYoRqTmcgzHcL9TCy1"
    }
