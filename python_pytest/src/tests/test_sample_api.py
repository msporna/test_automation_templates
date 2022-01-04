import pytest
from benedict import benedict
from deepdiff import DeepDiff


class TestSampleApi:


    @pytest.mark.smoke_api
    def test_valid_get_returns_200(self, api_manager):
        response = api_manager.make_get_request(endpoint="/versions")
        assert response.status_code == 200, f"status code is not 200! It is: {response.status_code}"

    @pytest.mark.smoke_api
    def test_get_versions_returns_expected_json(self, api_manager):
        response = api_manager.make_get_request(endpoint="/versions")
        response_data=benedict(response.text,format="json") # benedict allows us to find dict paths by providing string path
        assert response_data["values[0].title"]=="stable"
        assert response_data["values[0].ver"] == "96.0.4664.45"
        assert response_data["values[1].title"] == "beta"
        assert response_data["values[1].ver"] == "97.0.4692.36"


    @pytest.mark.smoke_api
    def test_new_version_can_be_created(self, api_manager,test_data_handler):
        new_version_payload= {"title": "test", "ver": "2021" }
        api_manager.make_post_request(endpoint="/versions", payload=new_version_payload)
        response_data_json = api_manager.make_get_request(endpoint="/versions").json()
        test_file_name="expected_response_1.json"
        test_data_json=test_data_handler.load_test_data_json(test_file_name)
        diff = DeepDiff(test_data_json, response_data_json, ignore_string_case=True,
                        ignore_order=True)
        assert str(
            diff) == "{}", f"There are differences between expected test data from {test_file_name} and response data"

    @pytest.mark.smoke_api
    def test_get_profile_returns_expected_json(self, api_manager):
        response = api_manager.make_get_request(endpoint="/profile")
        response_data = benedict(response.text,
                                 format="json")  # benedict allows us to find dict paths by providing string path
        assert response_data["name"] == "test"
        assert response_data["roles[0]"] == "admin"
        assert response_data["roles[1]"] == "user"
