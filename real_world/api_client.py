import requests


def fetch_json(url):
    """Fetch JSON from url, returning None on any request failure."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except ValueError:
        # BUG: only catches JSON-decode errors. Network failures like
        # requests.exceptions.ConnectionError / Timeout / HTTPError
        # are not caught here and propagate uncaught.
        return None
