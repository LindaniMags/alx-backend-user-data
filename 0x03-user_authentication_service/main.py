#!/usr/bin/env python3
"""End-to-end integration test
"""
import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """
    Tests register_user functionality
    """
    url = f"{BASE_URL}/users"
    data = {
        "email": email,
        "password": password,
    }
    res = requests.post(url, data=data)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}
    res = requests.post(url, data=data)
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Tests log_in_wrong_password functionality.
    """
    url = f"{BASE_URL}/sessions"
    data = {
        "email": email,
        "password": password,
    }
    res = requests.post(url, data=data)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Tests log_in functionality.
    """
    url = f"{BASE_URL}/sessions"
    data = {
        "email": email,
        "password": password,
    }
    res = requests.post(url, data=data, timeout=10)
    res.raise_for_status()
    assert res.json() == {"email": email, "message": "logged in"}
    session_id = res.cookies.get("session_id")
    if session_id is None:
        raise ValueError()
    return session_id


def profile_unlogged() -> None:
    """
    Tests profile_unlogged functionality.
    """
    url = f"{BASE_URL}/profile"
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Tests profile_logged functionality.
    """
    url = f"{BASE_URL}/profile"
    req_cookies = {'session_id': session_id}
    res = requests.get(url, cookies=req_cookies, timeout=10)
    res.raise_for_status()
    assert res.status_code == 200
    res_json = res.json()
    assert "email" in res_json


def log_out(session_id: str) -> None:
    """
    Tests log_out functionality.
    """
    url = f"{BASE_URL}/sessions"
    req_cookies = {
        "session_id": session_id,
    }
    res = requests.delete(url, cookies=req_cookies)
    assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """
    Tests reset_password_token functionality.
    """
    url = f"{BASE_URL}/reset_password"
    data = {"email": email}
    res = requests.post(url, data=data)
    assert res.status_code == 200
    res_json = res.json()
    assert "email" in res_json
    assert res_json["email"] == email
    assert "reset_token" in res_json
    return res_json["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Tests update_password functionality
    """
    url = f"{BASE_URL}/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }
    res = requests.put(url, data=data)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
