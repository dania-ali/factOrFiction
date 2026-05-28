import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_analyze_post_returns_200(client):
    response = client.post("/analyze", data={"claim": "The earth is flat."})
    assert response.status_code == 200


def test_analyze_echoes_claim(client):
    response = client.post("/analyze", data={"claim": "The earth is flat."})
    assert b"The earth is flat." in response.data


def test_analyze_empty_claim_no_500(client):
    response = client.post("/analyze", data={"claim": ""})
    assert response.status_code == 200


def test_analyze_empty_claim_no_echo(client):
    response = client.post("/analyze", data={"claim": ""})
    assert b"You submitted:" not in response.data


def test_home_has_form(client):
    response = client.get("/")
    assert b'action="/analyze"' in response.data
    assert b'name="claim"' in response.data


def test_nav_present_after_submit(client):
    response = client.post("/analyze", data={"claim": "Some claim"})
    assert b"Fact or Fiction" in response.data
    assert b'href="/"' in response.data
