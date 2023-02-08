from flask import Blueprint, redirect, request, abort, Response
import secrets
from dotenv import load_dotenv
import os
from urllib.parse import urlencode
import requests

load_dotenv()

bp = Blueprint("auth", __name__)


@bp.route("/login")
def login():
    state = secrets.token_hex(16)
    scope = "profile:read_all"

    url = "http://www.strava.com/oauth/authorize?"
    params = {
        "response_type": "code",
        "client_id": os.getenv("STRAVA_CLIENT_ID"),
        "scope": scope,
        "redirect_uri": os.getenv("STRAVA_REDIRECT_URI"),
        "approval_prompt": "force",
        "state": state
    }

    response = redirect(url + urlencode(params))
    response.set_cookie(key="strava_auth_state", value=state)
    return response


@bp.route("/callback")
def callback():
    code = request.args["code"]
    # state = request.args["state"]
    # stored_state = request.cookies.get("strava_auth_state")
    # if state is None or state != stored_state:
    #     abort(400)

    url = "https://www.strava.com/oauth/token?"
    params = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("STRAVA_CLIENT_ID"),
        "client_secret": os.getenv("STRAVA_CLIENT_SECRET"),
        "code": code
    }
    response = requests.post(url, params=params)
    # response.delete_cookie("strava_auth_state")

    if response.status_code == 200:
        data = response.json()
        access_token = data["access_token"]
        refresh_token = data["refresh_token"]
        response = redirect("http://localhost:5000/me")
        response.set_cookie(key="access_token", value=access_token)
        response.set_cookie(key="refresh_token", value=refresh_token)
        return response
