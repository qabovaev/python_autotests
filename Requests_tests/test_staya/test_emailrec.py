import pytest
import requests

staya_email = {"email":"qatest@staya.ru"}
url = "https://api.staya.dog/v1/auth/password/recovery/request"

def test_status_code():
    req = requests.post(url, data = staya_email)
    assert req.status_code == 200

def test_bodyrs():
    req = requests.post(url, data = staya_email)
    req = req.json()
    assert req["message"] == "Email sended"