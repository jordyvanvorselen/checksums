from behave import *


@when("I open the API documentation")
def step_impl(context):
    context.response = context.client.get("/docs")


@then("the API documentation will be returned")
def step_impl(context):
    assert context.response.status_code == 200
    assert b"<title>FastAPI - Swagger UI</title>" in context.response.content
