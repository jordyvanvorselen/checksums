from behave import fixture, use_fixture
from checksums.checksums import app
from fastapi.testclient import TestClient


@fixture
def client(context):
    client = TestClient(app)

    context.client = client

    yield client


def before_all(context):
    use_fixture(client, context)
