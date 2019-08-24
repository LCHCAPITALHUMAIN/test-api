# -*- coding: utf-8 -*-
import datetime
import os
import json
from pathlib import Path
import sys
import time
import unittest
from unittest import mock
import requests
from requests.exceptions import Timeout
import requests_mock
from loguru import logger
import pytest
from app.main import app
from app.com_lib.file_functions import open_json, save_json
from app.endpoints.sillyusers.gen_user import user_test_info

# from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

# from starlette.exceptions import HTTPException

client = TestClient(app)

directory_to__files: str = "data"


class test_default_endpoints(unittest.TestCase):
    def test_users_post_error(self):
        test_password = "testpassword"
        user_id = None
        userName = f"test-user-fail"

        test_data = {
            "user_name": userName,
            # "firstName": "string",
            "lastName": "string",
            "password": test_password,
            "title": "string",
            "company": "string",
            "address": "string",
            "city": "string",
            "country": "string",
            "postal": "string",
            "email": "string",
            "website": "string",
            "description": "string",
        }

        url = f"/api/v1/users/create/"
        client = TestClient(app)
        response = client.post(url, json=test_data)
        assert response.status_code == 422

    def test_users_post(self):
        test_user = user_test_info()
        save_json("test_data_test_user.json", test_user)
        url = f"/api/v1/users/create/?delay=1"
        client = TestClient(app)
        response = client.post(url, json=test_user)
        assert response.status_code == 200
        data = response.json()

        user_data = {
            "userId": data["userId"],
            "user_name": data["user_name"],
            "password": test_user["password"],
        }

        save_json("test_data_users.json", user_data)

    # def test_users_delete_delay(self):
    #     user_id = open_json("test_data_users.json")
    #     client = TestClient(app)
    #     response = client.delete(f"/api/v1/users/{user_id['userId']}?delay=1")
    #     assert response.status_code == 200
