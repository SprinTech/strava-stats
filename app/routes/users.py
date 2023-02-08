from flask import Blueprint, redirect, request, abort
import requests

bp = Blueprint("me", __name__)

BASE_URL = "https://www.strava.com/api/v3"


@bp.route("/me")
def get_user_information():
    access_token = request.cookies.get("access_token")
    url = BASE_URL + "/athlete"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()
