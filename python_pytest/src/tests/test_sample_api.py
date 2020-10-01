import pytest


class TestSampleApi:

    @pytest.mark.smoke
    def test_valid_get_returns_200(self, api_manager, disposable_example):
        response = api_manager.make_get_request("posts/1")
        print(disposable_example)  # this is just to show disposable_example fixture, not doing anything else
        # (the whole fixture and related print can be removed from this test and won't change its logic)
        assert response.status_code == 200, "status code is not 200!"

    @pytest.mark.smoke
    def test_get_returns_expected_json(self, api_manager, disposable_example):
        response = api_manager.make_get_request("posts/1")
        print(disposable_example)  # this is just to show disposable_example fixture, not doing anything else
        # (the whole fixture and related print can be removed from this test and won't change its logic)
        assert response.json()["title"] == "json-server", "response does not contain expected title!"
