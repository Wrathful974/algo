import sys, os
from unittest.mock import patch
import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from real_world.api_client import fetch_json


def test_returns_none_on_connection_error():
    with patch("requests.get", side_effect=requests.exceptions.ConnectionError):
        assert fetch_json("http://unreachable.example") is None


def test_returns_none_on_timeout():
    with patch("requests.get", side_effect=requests.exceptions.Timeout):
        assert fetch_json("http://slow.example") is None
