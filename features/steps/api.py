import json
from behave import *


@when("I do a POST request to {endpoint} with body")
def step_impl(context, endpoint):
    body = json.loads(context.text)
    response = context.client.post(endpoint, json=body)

    context.response = response


@then("the JSON response should be")
def step_impl(context):
    expected_response = json.loads(context.text)

    assert json.loads(context.response.text) == expected_response


@then("the response code should be {status_code}")
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)
