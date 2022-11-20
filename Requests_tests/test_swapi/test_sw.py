import pytest
import requests

url = "https://swapi.dev/api/people/13"

def test_status_code():
    req = requests.get(url)
    assert req.status_code == 200

def test_bodyrs():
    res = requests.get(url)
    res = res.json()
    assert res["name"] == "Chewbacca"

databody = [("height", "228", 13), ("name", "Luke Skywalker", 1), ("mass", "75", 2), ("eye_color", "yellow", 4)]
@pytest.mark.parametrize("key, value, id", databody)
def test_bodytext(key, value, id):
    url = f"https://swapi.dev/api/people/{id}"
    rq = requests.get(url)
    rq = rq.json()
    assert rq[key] == value