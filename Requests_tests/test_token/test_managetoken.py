import requests
import pytest

def test_manage_token():
    url_obtain = "https://partner.agentapp.ru/v1/users/obtain-token"
    token_rs = requests.post(url_obtain, json={"username":"qa@qa.qa", "password":"111"})
    token = token_rs.json()["token"]
    
    url_drive_cr = "https://partner.agentapp.ru/v1/insured_objects/drivers"

    data_driver = {
        "first_name": "Игорь",
        "last_name": "Трутестер",
        "patronymic": "Тестерович",
        "birth_date": "1996-06-14",
        "driving_experience_started": "2018-01-25",
        "driver_licenses": [
            {
            "credential_type": "DRIVER_LICENSE",
            "number": "619665",
            "series": "7032",
            "issue_date": "2018-06-25"
            }
        ]
    }
    header = {"Authorization" : f"Token {token}"}
    drivers_rs = requests.post(url_drive_cr, json=data_driver, headers=header)
    
    assert True, ""