from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_extract_text():
    URL = "http://google.com"
    response = client.get("/extract_text/?URL={}".format(URL))
    print(response.json())

def test_add_site():
    URL = "http://google.com"
    response = client.get("/extract_text/?URL={}".format(URL))
    print(response.json())


if __name__ == "__main__":
    test_extract_text()
