import json

from behave import step
from benedict import benedict
from deepdiff import DeepDiff
from features.src.pages.main_page import MainPage


@step('request is made')
def make_request(context):
    request_type = context.table.rows[0].get("request_type")
    endpoint = context.table.rows[0].get("endpoint")
    raw_payload = context.table.rows[0].get("payload", None)
    if raw_payload is not None:
        payload = json.loads(raw_payload)
    api_name = context.table.rows[0].get("api_name")

    if request_type.lower() == "get":
        context.cache["last_response"] = context.rest_api_handler.make_get_request(api_name, endpoint)
    elif request_type.lower() == "post":
        context.cache["last_response"] = context.rest_api_handler.make_post_request(api_name, endpoint,
                                                                                    payload=payload)


@step('the json response matches json from test data file "{test_file_name}"')
def compare_json_response_with_test_data(context, test_file_name):
    test_file_data = context.test_data_handler.load_test_data_json(test_file_name)
    diff = DeepDiff(test_file_data, context.cache["last_response"].json(), ignore_string_case=True,
                    ignore_order=True)
    assert str(
        diff) == "{}", f"There are differences between expected test data from {test_file_name} and response data"


@step('verify the status code is {expected_status_code}')
def verify_status_code(context, expected_status_code):
    last_response = context.cache["last_response"]
    assert last_response.status_code == int(
        expected_status_code), f"Response status code is not what was expected! It's {last_response.status_code} instead of {expected_status_code}"


@step('the json response contains')
def verify_json_response(context):
    last_response = context.cache["last_response"]
    for row in context.table:
        path = row.get("json_path")
        expected_value = row.get("expected_value")
        response_data = benedict(last_response.text,
                                 format='json')  # benedict supports accessing dict elements by `.` in path/ https://pypi.org/project/python-benedict/
        response_data_value_at_path = response_data[path]
        assert str(expected_value) == str(response_data_value_at_path), f"Expected value at path {path} is invalid!"
