import json

from behave import *


@then("the API documentation is returned")
def step_impl(context):
    assert b"<title>FastAPI - Swagger UI</title>" in context.response.content


@then("the API specification is returned")
def step_impl(context):
    assert "openapi" in json.loads(context.response.content).keys()
