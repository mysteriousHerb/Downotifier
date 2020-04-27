import requests
from bs4 import BeautifulSoup

chrome_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

def find_text_from_URL(URL, text_to_find):
    response = requests.get(URL, headers=chrome_headers)
    soup = BeautifulSoup(response.content, "lxml")

    if text_to_find in soup.text:
        return True
    else:
        return False


def extract_text_from_URL(URL):
    response = requests.get(URL, headers=chrome_headers)
    soup = BeautifulSoup(response.content, "lxml")

    return soup.text


if __name__ == '__main__':
    print(extract_text_from_URL("https://google.com/"))
    print(find_text_from_URL("https://google.com/", 'Google'))