from behave import fixture, use_fixture
from fastapi import FastAPI
from fastapi.testclient import TestClient


@fixture
def client(context):
    app = FastAPI()
    client = TestClient(app)

    context.client = client

    yield client


def before_all(context):
    use_fixture(client, context)
