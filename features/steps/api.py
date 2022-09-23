import json
import features

from pathlib import Path
from behave import *


@when("I do a GET request to {endpoint}")
def step_impl(context, endpoint):
    response = context.client.get(endpoint)
    context.response = response


@when("I do a POST request to {endpoint} with file {file_name}")
def step_impl(context, endpoint, file_name):
    with open(Path(features.__file__).parent / "templates" / file_name) as f:
        response = context.client.post(
            endpoint, files={"file": (file_name, f, "text/plain")}
        )

        context.response = response


@then("the JSON response should be")
def step_impl(context):
    expected_response = json.loads(context.text)

    assert json.loads(context.response.text) == expected_response


@then("the response code should be {status_code}")
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)
