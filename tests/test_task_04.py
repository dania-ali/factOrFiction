import pytest
from app import app
from analysis import analyze_claim


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# --- analyze_claim unit tests ---

def test_returns_required_keys():
    result = analyze_claim("some claim")
    assert "score" in result
    assert "label" in result
    assert "explanation" in result


def test_base_score_no_keywords():
    result = analyze_claim("the sky is blue")
    assert result["score"] == 50
    assert result["label"] == "Uncertain"


def test_positive_keyword_increases_score():
    result = analyze_claim("a new study confirms this")
    assert result["score"] > 50


def test_negative_keyword_decreases_score():
    result = analyze_claim("this is a hoax")
    assert result["score"] < 50


def test_multiple_positive_keywords():
    result = analyze_claim("study research evidence confirmed proven data")
    assert result["score"] == 100
    assert result["label"] == "Likely True"


def test_multiple_negative_keywords():
    result = analyze_claim("fake hoax scam lie lies debunked")
    assert result["score"] == 0
    assert result["label"] == "Likely False"


def test_score_clamped_above_100():
    # More positive keywords than points can accumulate past 100
    result = analyze_claim("study research evidence confirmed proven data data data")
    assert result["score"] <= 100


def test_score_clamped_below_0():
    result = analyze_claim("fake hoax scam lie lies debunked fake fake")
    assert result["score"] >= 0


def test_label_likely_true_at_60():
    result = analyze_claim("study research")  # 50 + 20 = 70
    assert result["label"] == "Likely True"


def test_label_likely_false_at_39_or_below():
    result = analyze_claim("fake hoax scam")  # 50 - 30 = 20
    assert result["label"] == "Likely False"


def test_whole_word_matching_no_partial():
    # "researcher" should not match "research"
    result = analyze_claim("the researcher published findings")
    assert result["score"] == 50


def test_case_insensitive_matching():
    result_lower = analyze_claim("study")
    result_upper = analyze_claim("STUDY")
    assert result_lower["score"] == result_upper["score"]


def test_empty_string_returns_uncertain():
    result = analyze_claim("")
    assert result["score"] == 50
    assert result["label"] == "Uncertain"


def test_whitespace_only_returns_uncertain():
    result = analyze_claim("   ")
    assert result["score"] == 50
    assert result["label"] == "Uncertain"


def test_explanation_is_string():
    result = analyze_claim("some claim here")
    assert isinstance(result["explanation"], str)
    assert len(result["explanation"]) > 0


# --- Integration tests via Flask client ---

def test_result_shown_after_submit(client):
    response = client.post("/analyze", data={"claim": "study research evidence"})
    assert b"Score:" in response.data
    assert b"Verdict:" in response.data


def test_likely_true_label_in_response(client):
    response = client.post("/analyze", data={"claim": "study research evidence confirmed"})
    assert b"Likely True" in response.data


def test_likely_false_label_in_response(client):
    response = client.post("/analyze", data={"claim": "fake hoax scam lies"})
    assert b"Likely False" in response.data


def test_placeholders_shown_on_home(client):
    response = client.get("/")
    assert b"Analysis breakdown will appear here" in response.data
    assert b"Credibility score and verdict will appear here" in response.data


def test_placeholders_hidden_after_submit(client):
    response = client.post("/analyze", data={"claim": "study"})
    assert b"Analysis breakdown will appear here" not in response.data
    assert b"Credibility score and verdict will appear here" not in response.data
