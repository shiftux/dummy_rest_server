import os
import pytest
import requests

if os.getenv('RUNNING_ON_K8S') == 'yes':
    host = 'rest-routes.twint.svc.cluster.local'
    port = 80
elif os.getenv('RUNNING_IN_DOCKER') == 'yes':
    host = 'rest_routes'
    port = 3000
else:
    host = '127.0.0.1'
    port = 5000

endpoints = [
    "dirk",
    "erich",
    "ueli",
    "michi",
    "sandro",
]


@pytest.mark.parametrize("endpoint", endpoints)
def test_status200(endpoint):
    address = f"http://{host}:{port}/{endpoint}"
    print(f"address is :  {address}")
    response = requests.get(address)
    assert response.status_code == 200


replies = [
    ("dirk", "Global-Galaktisch\n"),
    ("ueli", "Ich möchte auch so eine Frisur haben wie Dirk\n"),
    ("michi", "Ich hasse Powerpoint\n"),
    ("erich", "Maslov hat das WiFi ganz unten in der Pyramide vergessen\n"),
    ("sandro", "Cloud mover!!!\n")
]


@pytest.mark.parametrize("endpoint, reply", replies)
def test_replies(endpoint, reply):
    address = f"http://{host}:{port}/{endpoint}"
    print(f"address is :  {address}")
    response = requests.get(address)
    assert response.text == reply
